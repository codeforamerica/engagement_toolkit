#!/usr/bin/python

"""
Natural Language Processing of Likeminded text submissions
Using cosine similarity
This is refactored code from Mining the Social Web by Matthew A. Russell, published by O'Reilly Media, Inc. Print ISBN-13: 978-1-4493-8834-8
"""

import sys
import couchdb
import nltk
import json

#Load in data from couch

server = couchdb.Server('localhost:5984')
db = server['likeminded']

likeminded_data = db.query('function(doc) { emit(doc._id, doc); }')

docs = [' '.join([row.value['name'],
                  row.value['problem'] or '',
                  row.value['process'] or '',
                  row.value['result'] or '']) for row in likeminded_data]

all_posts = [post.lower().split() for post in docs]

# Provides tf/idf/tf_idf abstractions for scoring

tc = nltk.TextCollection(all_posts)

# Compute a term-document matrix such that td_matrix[doc_title][term]
# returns a tf-idf score for the term in the document

td_matrix = {}
for idx in range(len(all_posts)):
    post = all_posts[idx]
    fdist = nltk.FreqDist(post)

    doc_title = list(likeminded_data)[idx].value['name']
    link = list(likeminded_data)[idx].value['link']
    td_matrix[(doc_title, link)] = {}

    for term in fdist.iterkeys():
        td_matrix[(doc_title, link)][term] = tc.tf_idf(term, post)

# Build vectors such that term scores are in the same positions...

distances = {}
for (title1, link1) in td_matrix.keys():

    distances[(title1, link1)] = {}
    (max_score, most_similar) = (0.0, (None, None))

    for (title2, link2) in td_matrix.keys():

        # Take care not to mutate the original data structures
        # since we're in a loop and need the originals multiple times

        terms1 = td_matrix[(title1, link1)].copy()
        terms2 = td_matrix[(title2, link2)].copy()

        # Fill in "gaps" in each map so vectors of the same length can be computed

        for term1 in terms1:
            if term1 not in terms2:
                terms2[term1] = 0

        for term2 in terms2:
            if term2 not in terms1:
                terms1[term2] = 0

        # Create vectors from term maps

        v1 = [score for (term, score) in sorted(terms1.items())]
        v2 = [score for (term, score) in sorted(terms2.items())]

        # Compute similarity among documents

        distances[(title1, link1)][(title2, link2)] = \
            nltk.cluster.util.cosine_distance(v1, v2)

        if link1 == link2:
            continue
        if distances[(title1, link1)][(title2, link2)] > max_score:
            (max_score, most_similar) = (distances[(title1, link1)][(title2,
                                         link2)], (title2, link2))

#    print '''Most similar to %s (%s)
#\t%s (%s)
#\tscore %s
#''' % (title1, link1,
#            most_similar[0], most_similar[1], max_score)

    print '"%s","%s","%s","%s",%s' % (title1, link1,
            most_similar[0], most_similar[1], max_score)
