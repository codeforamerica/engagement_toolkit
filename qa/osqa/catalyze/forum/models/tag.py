import datetime
from base import *

from django.utils.translation import ugettext as _
from django.utils.encoding import smart_unicode, force_unicode

from forum import modules

class ActiveTagManager(CachedManager):
    use_for_related_fields = True

    def get_query_set(self):
        return super(ActiveTagManager, self).get_query_set().exclude(used_count__lt=1)

class Tag(BaseModel):
    name            = models.CharField(max_length=255, unique=True)
    created_by      = models.ForeignKey(User, related_name='created_tags')
    created_at      = models.DateTimeField(default=datetime.datetime.now, blank=True, null=True)
    marked_by       = models.ManyToManyField(User, related_name="marked_tags", through="MarkedTag")
    # Denormalised data
    used_count = models.PositiveIntegerField(default=0)

    active = ActiveTagManager()

    class Meta:
        ordering = ('-used_count', 'name')
        app_label = 'forum'

    def __unicode__(self):
        return force_unicode(self.name)

    def add_to_usage_count(self, value):
        if self.used_count + value < 0:
            self.used_count = 0
        else:
            self.used_count = models.F('used_count') + value

    def cache_key(self):
        return self._generate_cache_key(Tag.safe_cache_name(self.name))

    @classmethod
    def safe_cache_name(cls, name):
        return "".join([str(ord(c)) for c in name])

    @classmethod
    def infer_cache_key(cls, querydict):
        if 'name' in querydict:
            return cls._generate_cache_key(cls.safe_cache_name(querydict['name']))

        return None

    @classmethod
    def value_to_list_on_cache_query(cls):
        return 'name'

    @models.permalink
    def get_absolute_url(self):
        return ('tag_questions', (), {'tag': self.name})

class MarkedTag(models.Model):
    TAG_MARK_REASONS = (('good', _('interesting')), ('bad', _('ignored')))
    tag = models.ForeignKey(Tag, related_name='user_selections')
    user = models.ForeignKey(User, related_name='tag_selections')
    reason = models.CharField(max_length=16, choices=TAG_MARK_REASONS)

    class Meta:
        app_label = 'forum'

