from django.core.management.base import NoArgsCommand
from forum.models import *
from forum.actions import *
import datetime

class Command(NoArgsCommand):
    
    def handle_noargs(self, **options):
        question = self._ask()
        self._answer(question)
        
    
    def _ask(self):
        #retrieve the "asker" from the database
        user = User.objects.all()[0]

        #prepare question data
        qdata = dict(
            title = "This is a sample imported question",
            text = "I have stuff to do, just don't know how.",
            tags = "philadelphia",
        )

        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        ask = AskAction(user=user).save(data=qdata)
        return ask.node
        
    
    def _answer(self, question):
        #retrieve the "answerer" from the database
        user = User.objects.all()[0]
        
        #prepare question data
        adata = dict(
            text = "blah",
            question = question
        )
        
        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        AnswerAction(user=user).save(data=adata)

