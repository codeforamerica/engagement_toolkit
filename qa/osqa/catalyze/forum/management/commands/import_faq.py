from django.core.management.base import NoArgsCommand
from forum.models import *
from forum.actions import *
import datetime

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        #retrieve the "asker" from the database
        user = User.objects.get(id="9")

        #prepare question data
        qdata = dict(
            title = "This is a sample imported question",
            text = "I have stuff to do, just don't know how.",
            tags = "philadelphia",
        )

        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        question = AskAction(user=user).save(data=qdata)
        print question.node
