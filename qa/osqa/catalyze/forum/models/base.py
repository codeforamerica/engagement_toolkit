import datetime
import re
try:
    from hashlib import md5
except:
    from md5 import new as md5
from urllib import quote_plus, urlencode
from django.db import models, IntegrityError, connection, transaction
from django.utils.http import urlquote  as django_urlquote
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.template.defaultfilters import slugify
from django.db.models.signals import post_delete, post_save, pre_save, pre_delete
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib.sitemaps import ping_google
import django.dispatch
from forum import settings
import logging


if not hasattr(cache, 'get_many'):
    #put django 1.2 code here
    pass

class LazyQueryList(object):
    def __init__(self, model, items):
        self.items = items
        self.model = model

    def __getitem__(self, k):
        return self.model.objects.get(id=self.items[k][0])

    def __iter__(self):
        for id in self.items:
            yield self.model.objects.get(id=id[0])

    def __len__(self):
        return len(self.items)

class ToFetch(str):
    pass

class CachedQuerySet(models.query.QuerySet):

    def lazy(self):
        if not len(self.query.aggregates):
            values_list = ['id']

            if len(self.query.extra):
                extra_keys = self.query.extra.keys()
                values_list += extra_keys

            return LazyQueryList(self.model, list(self.values_list(*values_list)))
        else:
            return self

    def obj_from_datadict(self, datadict):
        obj = self.model()
        obj.__dict__.update(datadict)

        if hasattr(obj, '_state'):
            obj._state.db = 'default'

        return obj

    def _base_clone(self):
        return self._clone(klass=models.query.QuerySet)

    def get(self, *args, **kwargs):
        key = self.model.infer_cache_key(kwargs)

        if key is not None:
            obj = cache.get(key)

            if obj is None:
                obj = self._base_clone().get(*args, **kwargs)
                obj.cache()
            else:
                obj = self.obj_from_datadict(obj)
                obj.reset_original_state()

            return obj

        return self._base_clone().get(*args, **kwargs)

    def _fetch_from_query_cache(self, key):
        invalidation_key = self.model._get_cache_query_invalidation_key()
        cached_result = cache.get_many([invalidation_key, key])

        if not invalidation_key in cached_result:
            self.model._set_query_cache_invalidation_timestamp()
            return None

        if (key in cached_result) and(cached_result[invalidation_key] < cached_result[key][0]):
            return cached_result[key][1]

        return None

    def count(self):
        cache_key = self.model._generate_cache_key("CNT:%s" % self._get_query_hash())
        result = self._fetch_from_query_cache(cache_key)

        if result is not None:
            return result

        result = super(CachedQuerySet, self).count()
        cache.set(cache_key, (datetime.datetime.now(), result), 60 * 60)
        return result

    def iterator(self):
        cache_key = self.model._generate_cache_key("QUERY:%s" % self._get_query_hash())
        on_cache_query_attr = self.model.value_to_list_on_cache_query()

        to_return = None
        to_cache = {}

        key_list = self._fetch_from_query_cache(cache_key)

        if key_list is None:
            if not len(self.query.aggregates):
                values_list = [on_cache_query_attr]

                if len(self.query.extra):
                    values_list += self.query.extra.keys()

                key_list = [v[0] for v in self.values_list(*values_list)]
                to_cache[cache_key] = (datetime.datetime.now(), key_list)
            else:
                to_return = list(super(CachedQuerySet, self).iterator())
                to_cache[cache_key] = (datetime.datetime.now(), [row.__dict__[on_cache_query_attr] for row in to_return])

        if (not to_return) and key_list:
            row_keys = [self.model.infer_cache_key({on_cache_query_attr: attr}) for attr in key_list]
            cached = cache.get_many(row_keys)

            to_return = [
                (ck in cached) and self.obj_from_datadict(cached[ck]) or ToFetch(key_list[i]) for i, ck in enumerate(row_keys)
            ]

            if len(cached) != len(row_keys):
                to_fetch = [str(tr) for tr in to_return if isinstance(tr, ToFetch)]

                fetched = dict([(str(r.__dict__[on_cache_query_attr]), r) for r in
                              models.query.QuerySet(self.model).filter(**{"%s__in" % on_cache_query_attr: to_fetch})])

                to_return = [(isinstance(tr, ToFetch) and fetched[str(tr)] or tr) for tr in to_return]
                to_cache.update(dict([(self.model.infer_cache_key({on_cache_query_attr: attr}), r._as_dict()) for attr, r in fetched.items()]))


        if len(to_cache):
            cache.set_many(to_cache, 60 * 60)

        if to_return:
            for row in to_return:
                if hasattr(row, 'leaf'):
                    yield row.leaf
                else:
                    yield row

    def _get_query_hash(self):
        return md5(unicode(self.query).encode("utf-8")).hexdigest()



class CachedManager(models.Manager):
    use_for_related_fields = True

    def get_query_set(self):
        return CachedQuerySet(self.model)

    def get_or_create(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except:
            return super(CachedManager, self).get_or_create(*args, **kwargs)


class DenormalizedField(object):
    def __init__(self, manager, *args, **kwargs):
        self.manager = manager
        self.filter = (args, kwargs)

    def setup_class(self, cls, name):
        dict_name = '_%s_dencache_' % name

        def getter(inst):
            val = inst.__dict__.get(dict_name, None)

            if val is None:
                val = getattr(inst, self.manager).filter(*self.filter[0], **self.filter[1]).count()
                inst.__dict__[dict_name] = val
                inst.cache()

            return val

        def reset_cache(inst):
            inst.__dict__.pop(dict_name, None)
            inst.uncache()

        cls.add_to_class(name, property(getter))
        cls.add_to_class("reset_%s_cache" % name, reset_cache)


class BaseMetaClass(models.Model.__metaclass__):
    to_denormalize = []

    def __new__(cls, *args, **kwargs):
        new_cls = super(BaseMetaClass, cls).__new__(cls, *args, **kwargs)

        BaseMetaClass.to_denormalize.extend(
            [(new_cls, name, field) for name, field in new_cls.__dict__.items() if isinstance(field, DenormalizedField)]
        )

        return new_cls

    @classmethod
    def setup_denormalizes(cls):
        for new_cls, name, field in BaseMetaClass.to_denormalize:
            field.setup_class(new_cls, name)


class BaseModel(models.Model):
    __metaclass__ = BaseMetaClass

    objects = CachedManager()

    class Meta:
        abstract = True
        app_label = 'forum'

    def __init__(self, *args, **kwargs):
        super(BaseModel, self).__init__(*args, **kwargs)
        self.reset_original_state(kwargs.keys())

    def reset_original_state(self, reset_fields=None):
        self._original_state = self._as_dict()
        
        if reset_fields:
            self._original_state.update(dict([(f, None) for f in reset_fields]))

    def get_dirty_fields(self):
        return [f.name for f in self._meta.fields if self._original_state[f.attname] != self.__dict__[f.attname]]

    def _as_dict(self):
        return dict([(name, getattr(self, name)) for name in
                     ([f.attname for f in self._meta.fields] + [k for k in self.__dict__.keys() if k.endswith('_dencache_')])
        ])

    def _get_update_kwargs(self):
        return dict([
            (f.name, getattr(self, f.name)) for f in self._meta.fields if self._original_state[f.attname] != self.__dict__[f.attname]
        ])

    def save(self, full_save=False, *args, **kwargs):
        put_back = [k for k, v in self.__dict__.items() if isinstance(v, models.expressions.ExpressionNode)]

        if hasattr(self, '_state'):
            self._state.db = 'default'

        if self.id and not full_save:
            self.__class__.objects.filter(id=self.id).update(**self._get_update_kwargs())
        else:
            super(BaseModel, self).save()

        if put_back:
            try:
                self.__dict__.update(
                    self.__class__.objects.filter(id=self.id).values(*put_back)[0]
                )
            except:
                logging.error("Unable to read %s from %s" % (", ".join(put_back), self.__class__.__name__))
                self.uncache()

        self.reset_original_state()
        self._set_query_cache_invalidation_timestamp()
        self.cache()

    @classmethod
    def _get_cache_query_invalidation_key(cls):
        return cls._generate_cache_key("INV_TS")

    @classmethod
    def _set_query_cache_invalidation_timestamp(cls):
        cache.set(cls._get_cache_query_invalidation_key(), datetime.datetime.now(), 60 * 60 * 24)

        for base in filter(lambda c: issubclass(c, BaseModel) and (not c is BaseModel), cls.__bases__):
            base._set_query_cache_invalidation_timestamp()

    @classmethod
    def _generate_cache_key(cls, key, group=None):
        if group is None:
            group = cls.__name__

        return '%s:%s:%s' % (settings.APP_URL, group, key)

    def cache_key(self):
        return self._generate_cache_key(self.id)

    @classmethod
    def value_to_list_on_cache_query(cls):
        return 'id'

    @classmethod
    def infer_cache_key(cls, querydict):
        try:
            pk = [v for (k,v) in querydict.items() if k in ('pk', 'pk__exact', 'id', 'id__exact'
                            ) or k.endswith('_ptr__pk') or k.endswith('_ptr__id')][0]

            return cls._generate_cache_key(pk)
        except:
            return None

    def cache(self):
        cache.set(self.cache_key(), self._as_dict(), 60 * 60)

    def uncache(self):
        cache.delete(self.cache_key())

    def delete(self):
        self.uncache()
        self._set_query_cache_invalidation_timestamp()
        super(BaseModel, self).delete()


from user import User
from node import Node, NodeRevision, NodeManager
from action import Action





