from django.db import models

import forum.models

# Create your models here.
class Faq(models.Model):
    url = models.CharField(max_length=2048)

class FaqItem(models.Model):
    faq = models.ForeignKey('Faq', related_name='items')
    number = models.IntegerField()
    create_date = models.DateTimeField(null=True)
    question = models.OneToOneField(forum.models.Question, null=True)
    answer = models.OneToOneField(forum.models.Answer, null=True)

