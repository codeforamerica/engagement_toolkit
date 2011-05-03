from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _

from views import updater_index, updater_check

urlpatterns = patterns('',
    url(r'^%s%s%s$' % (_('admin/'), _('updater/'), _('check/')),  updater_check, name='updater_check'),
)
