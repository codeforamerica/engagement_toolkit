import django.db.utils
import csv
import datetime
import ingredients.models
import forum.models
import forum.actions

class FaqDataFromCsv(object):
    reader = csv.reader
    
    def __init__(self, csv_stream):
        self.__stream = csv_stream
    
    def _ask(self, user, title, text='', tags=''):
        #retrieve the "asker" from the database
#        user = User.objects.all()[0]

        #prepare question data
        qdata = dict(
            title = title,
            text = text,
            tags = tags,
        )

        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        ask = forum.actions.AskAction(user=user).save(data=qdata)
        return ask.node
        
    
    def _answer(self, user, question, text):
        #retrieve the "answerer" from the database
#        user = User.objects.all()[0]
        
        #prepare question data
        adata = dict(
            text = text,
            question = question
        )
        
        #save the question, everything will be handled internally,
        #like creating the tags if they don't exist, etc 
        answer = forum.actions.AnswerAction(user=user).save(data=adata)
        return answer.node
    
    def save(self, username):
    
        faqs = set()
        
        first_skipped = False
        for row in csv.reader(self.__stream):
            print row
            if not first_skipped:
                first_skipped = True
                continue
            
            # Pull out the question data
            url = row[0]
            create_date = row[1]
            question_number = row[2]
            question = row[3]
            answer = row[4]
            
            # Create the faq, if it does not already exist
            faq, _ = ingredients.models.Faq.objects.get_or_create(
                url = url
            )
            
            # Check whether there is already an item on the faq with the given
            # question number.  If so, skip this one.
            item, created = ingredients.models.FaqItem.objects.get_or_create(
                faq = faq,
                number = int(question_number)
            )
            
            if not created:
                continue
            
            # Ask the question and provide the answer, by the appropriate user.
            user = forum.models.User.objects.get(username=username)
            
            while True:
                try:
                    item.question = self._ask(
                        user,
                        question,
                        ''
                    )
                    item.answer = self._answer(
                        user,
                        item.question,
                        answer + '\n\n[%s](%s)' % (url,url)
                    )
                    item.save()
                    break
                except django.db.utils.DatabaseError:
                    continue
                        
            faqs.add(faq)
            
        return faqs
