from django.contrib.sitemaps import Sitemap
from forum.models import Question
from forum.settings import QUESTIONS_SITEMAP_LIMIT, QUESTIONS_SITEMAP_CHANGEFREQ
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template import loader
from django.core import urlresolvers
from django.utils.encoding import smart_str
from django.core.paginator import EmptyPage, PageNotAnInteger

def index(request, sitemaps):
    sites = []
    for section, site in sitemaps.items():
        if callable(site):
            pages = site().paginator.num_pages
        else:
            pages = site.paginator.num_pages
        sitemap_url = urlresolvers.reverse('sitemap_section_index', kwargs={'section': section})
        sites.append('%s%s' % (settings.APP_URL, sitemap_url))

    xml = loader.render_to_string('sitemap_index.xml', {'sitemaps': sites})
    return HttpResponse(xml, mimetype='application/xml')

def sitemap_section_index(request, section, sitemaps):
    try:
        sitemap = sitemaps[section]()
    except KeyError:
        raise Http404("Sitemap doesn't exist")

    paginator = sitemap.paginator

    locations = []

    for page in paginator.page_range:
        location = urlresolvers.reverse('sitemap_section_page', kwargs={ 'page' : page, 'section' : section })
        location = '%s%s' % (settings.APP_URL, location)
        locations.append(location)

    xml = loader.render_to_string('sitemap_section_index.xml', { 'locations' : locations, })
    return HttpResponse(xml, mimetype='application/xml')

def sitemap(request, sitemaps, section=None, page=1):
    maps, urls = [], []
    if section is not None:
        if section not in sitemaps:
            raise Http404("No sitemap available for section: %r" % section)
        maps.append(sitemaps[section])
    else:
        maps = sitemaps.values()
    
    for site in maps:
        try:
            if callable(site):
                urls.extend(site().get_urls(page=page))
            else:
                urls.extend(site.get_urls(page=page))
        except EmptyPage:
            raise Http404("Page %s empty" % page)
        except PageNotAnInteger:
            raise Http404("No page '%s'" % page)
    xml = smart_str(loader.render_to_string('sitemap.xml', {'urlset': urls}))
    return HttpResponse(xml, mimetype='application/xml')

class OsqaSitemap(Sitemap):
    limit = QUESTIONS_SITEMAP_LIMIT
    changefreq = QUESTIONS_SITEMAP_CHANGEFREQ
    priority = 0.5
    def items(self):
        return Question.objects.filter_state(deleted=False).order_by('id')

    def lastmod(self, obj):
        return obj.last_activity_at

    def location(self, obj):
        return obj.get_absolute_url()

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def get_urls(self, page=1):
        urls = []
        for item in self.paginator.page(page).object_list:
            loc = "%s%s" % (settings.APP_URL, self.__get('location', item))
            url_info = {
                'location':   loc,
                'lastmod':    self.__get('lastmod', item, None),
                'changefreq': self.__get('changefreq', item, None),
                'priority':   self.__get('priority', item, None)
            }
            urls.append(url_info)
        return urls
