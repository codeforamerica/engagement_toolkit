from django.core.management.base import NoArgsCommand
from forum.models import *
from forum.actions import *
import datetime

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        #retrieve the "asker" from the database
        user = User.objects.get(id="1")

        #prepare question data
        qdata = dict(
            title = "This is a sample imported question"
            text = "I have stuff to do, just don't know how.",
            tagnames = "test philly",
        )

        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        AskAction(user=user).save(data=qdata)
