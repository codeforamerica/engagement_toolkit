import datetime
import views
import logging
import settings

from xml.dom.minidom import parse, parseString
from xml.parsers.expat import ExpatError
from forum.modules import ui, decorate
from forum.settings import SVN_REVISION
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_str

from base import update_trigger

# Update the user messages
@decorate.result(AuthenticationMiddleware.process_request, needs_params=True)
def process_request(result, self, request):
    # Call the update trigger on every request
    update_trigger()

    try:
        messages_dom = parseString(smart_str(settings.UPDATE_MESSAGES_XML.value))
        messages = messages_dom.getElementsByTagName('message')

        for message in messages:
            # Get the SVN Revision
            try:
                svn_revision = int(SVN_REVISION.replace('SVN-', ''))
            except ValueError:
                # Here we'll have to find another way of getting the SVN revision
                svn_revision = 0

            message_body = message.getElementsByTagName('body')[0].firstChild.nodeValue
            message_revision = int(message.getElementsByTagName('revision')[0].firstChild.nodeValue)

            # Add the message to the user messages set only if the Message Revision number is greater than the
            # current installation SVN Revision number and only if the current user is a super user.
            if message_revision >= svn_revision and request.user.is_superuser:
                # We do not want to repeat ourselves. If the message already exists in the message list, we're not going to
                # add it. That's why first of all we're going the check if it is there.
                try:
                    # If the message doesn't exist in the RelatedManager ObjectsDoesNotExist is going to be raised.
                    request.user.message_set.all().get(message=message_body)
                except ObjectDoesNotExist:
                    # Let's create the message.
                    request.user.message_set.create(message=message_body)
                except:
                    pass
    except ExpatError:
        pass

    return result