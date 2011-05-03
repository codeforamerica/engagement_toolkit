# -*- coding: utf-8 -*-

import sys
import json
import nltk

# Load in textual data from wherever you've saved it

BUZZ_DATA = sys.argv[1]
buzz_data = json.loads(open(BUZZ_DATA).read())

all_posts = [post['content'].lower().split() for post in buzz_data]

# Provides tf/idf/tf_idf abstractions for scoring

tc = nltk.TextCollection(all_posts)

# Compute a term-document matrix such that td_matrix[doc_title][term]
# returns a tf-idf score for the term in the document

td_matrix = {}
for idx in range(len(all_posts)):
    post = all_posts[idx]
    fdist = nltk.FreqDist(post)

    doc_title = buzz_data[idx]['content']
#    link = buzz_data[idx]['link']
    td_matrix[(doc_title)] = {}

    for term in fdist.iterkeys():
        td_matrix[(doc_title)][term] = tc.tf_idf(term, post)

# Build vectors such that term scores are in the same positions...

distances = {}

for (title1) in td_matrix.keys():

    distances[(title1)] = {}
    (max_score, most_similar) = (0.0, (None, None))

    for (title2) in td_matrix.keys():

        # Take care not to mutate the original data structures
        # since we're in a loop and need the originals multiple times

        terms1 = td_matrix[(title1)].copy()
        terms2 = td_matrix[(title2)].copy()

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

        distances[(title1)][(title2)] = \
            nltk.cluster.util.cosine_distance(v1, v2)

        if distances[(title1)][(title2)] > max_score:
            (max_score, most_similar) = (distances[(title1)][(title2)], (title2))

	print title1
	print most_similar
	print max_score