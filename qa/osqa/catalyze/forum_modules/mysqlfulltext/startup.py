from django.db import connection, transaction
import os, settings

import re
from django.db import connection, transaction, models
from django.db.models import Q
from forum.models.question import Question, QuestionManager
from forum.models.node import Node
from forum.modules import decorate

if not bool(settings.MYSQL_FTS_INSTALLED):
    f = open(os.path.join(os.path.dirname(__file__), 'fts_install.sql'), 'r')

    try:
        cursor = connection.cursor()
        cursor.execute(f.read())
        transaction.commit_unless_managed()

        settings.MYSQL_FTS_INSTALLED.set_value(True)

    except Exception, e:
        #import sys, traceback
        #traceback.print_exc(file=sys.stdout)
        pass
    finally:
        cursor.close()

    f.close()

word_re = re.compile(r'\w+', re.UNICODE)

@decorate(QuestionManager.search, needs_origin=False)
def question_search(self, keywords):
    return False, self.filter(models.Q(ftsindex__body__search=keywords.upper()))