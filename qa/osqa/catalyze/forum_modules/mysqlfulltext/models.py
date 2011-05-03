from django.db import models

class MysqlFtsIndex(models.Model):
    node       = models.OneToOneField('Node', related_name='ftsindex')
    body       = models.TextField()

    class Meta:
        managed = False
        app_label = 'forum'