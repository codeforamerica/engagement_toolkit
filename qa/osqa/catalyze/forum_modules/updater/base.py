import os
import sys
import bz2
import urllib2, urllib
import binascii
import string
import random
import re
import urllib2
import settings
import datetime
import logging


from xml.dom.minidom import parse, parseString
from forum.models import Question, User
from forum.settings import APP_URL, SVN_REVISION
from django import VERSION as DJANGO_VERSION
from django.utils import simplejson
from django.utils.encoding import smart_unicode
from django.conf import settings as django_settings
from django.utils.translation import ugettext as _


def generate_installation_key():
    gen = lambda length: "".join( [random.choice(string.digits+string.letters) for i in xrange(length)])
    return '%s-%s-%s-%s' % (gen(4), gen(4), gen(4), gen(4))

# To get the site views count we get the SUM of all questions views.
def get_site_views():
    views = 0

    # Go through all questions and increase the views count
    for question in Question.objects.all():
        views += question.view_count

    return views

def get_server_name():
    url = '%s/' % APP_URL

    try:
        # Make the request
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        # Get the response information
        response_info = response.info()

        server_name = re.findall("Server: (?P<server_name>.*)$", str(response_info))[0]
        server_name = ''.join(server_name.splitlines())

        return server_name
    except:
        return 'Unknown'

def get_admin_emails():
    emails = []

    for user in User.objects.filter(is_superuser=True):
        emails.append(user.email)

    return emails

def check_for_updates():
    # Get the SVN Revision
    try:
        svn_revision = int(SVN_REVISION.replace('SVN-', ''))
    except ValueError:
        # Here we'll have to find another way of getting the SVN revision
        svn_revision = 0

    admin_emails_xml = '<emails>'
    for email in get_admin_emails():
        admin_emails_xml += '<email value="%s" />' % email
    admin_emails_xml += '</emails>'

    statistics = """<check>
    <key value="%(site_key)s" />
    <app_url value="%(app_url)s" />
    <svn_revision value="%(svn_revision)d" />
    <views value="%(site_views)d" />
    <active_users value="11959" />
    <server value="%(server_name)s" />
    <python_version value="%(python_version)s" />
    <django_version value="%(django_version)s" />
    <database value="%(database)s" />
    <os value="%(os)s" />
    %(emails)s
</check> """ % {
        'site_key' : settings.SITE_KEY,
        'app_url' : APP_URL,
        'svn_revision' : svn_revision,
        'site_views' : get_site_views(),
        'server_name' : get_server_name(),
        'python_version' : ''.join(sys.version.splitlines()),
        'django_version' : str(DJANGO_VERSION),
        'database' : django_settings.DATABASE_ENGINE,
        'os' : str(os.uname()),
        'emails' : admin_emails_xml,
    }

    # Compress the statistics XML dump
    statistics_compressed = bz2.compress(statistics)

    # Pass the compressed statistics to the update server
    post_data = {
        'statistics' : binascii.b2a_base64(statistics_compressed),
    }
    data = urllib.urlencode(post_data)

    # We simulate some browser, otherwise the server can return 403 response
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-us) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/5'
    headers={ 'User-Agent' : user_agent,}

    try:
        check_request = urllib2.Request('%s%s' % (settings.UPDATE_SERVER_URL, '/site_check/'), data, headers=headers)
        check_response = urllib2.urlopen(check_request)
        content = check_response.read()
    except urllib2.HTTPError, error:
        content = error.read()

    # Read the messages from the Update Server
    messages_xml_url = '%s%s' % (settings.UPDATE_SERVER_URL, '/messages/xml/')
    messages_request = urllib2.Request(messages_xml_url, headers=headers)
    messages_response = urllib2.urlopen(messages_request)
    messages_xml = messages_response.read()

    # Store the messages XML in a Setting object
    settings.UPDATE_MESSAGES_XML.set_value(messages_xml)

    messages_dom = parseString(messages_xml)
    messages_count = len(messages_dom.getElementsByTagName('message'))

    return _('%d update messages have been downloaded') % messages_count

def update_trigger():
    # Trigger the update process
    now = datetime.datetime.now()
    if (now - settings.LATEST_UPDATE_DATETIME) > datetime.timedelta(days=1):
        update_status = check_for_updates()

        logging.error(smart_unicode("Update process has been triggered: %s" % update_status))

        # Set the latest update datetime to now.
        settings.LATEST_UPDATE_DATETIME.set_value(now)
