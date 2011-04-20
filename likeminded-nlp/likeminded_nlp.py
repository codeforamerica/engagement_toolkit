#!/usr/bin/python

"""
Natural Language Processing of Likeminded text submissions
using cosine similarity
This is refactored code from Mining the Social Web by Matthew A. Russell, published by O'Reilly Media, Inc. Print ISBN-13: 978-1-4493-8834-8
"""

import sys
import couchdb
import MySQLdb as mysqldb
import nltk
import json

def LikeMindedDataLoaderFactory(dl_type, *args, **kwds):
    """Creates a LikeMindedDataLoader based on the given type string.
    
    Type strings:
    'couch'
    'mysql'
    
    """
    if dl_type.lower() == 'couch':
        return CouchDataLoader(*args, **kwds)
    elif dl_type.lower() == 'mysql':
        return MySQLDataLoader(*args, **kwds)
    else:
        raise ValueError("Don't know what a %r loader is" % dl_type)

class LikeMindedDataLoader (object):
    
    def get_likeminded_data(self):
        """Builds a list of strings, each containing the text of a project.
        
        For each LikeMinded project in the data store, the name, problem 
        statement, process, and result are joined into one string.  Returns a
        list of these strings.
        """
        docs = [' '.join([row.value['name'],
                          row.value['problem'] or '',
                          row.value['process'] or '',
                          row.value['result'] or '']) 
                          for row in self.likeminded_data]
        
        return docs
    
    def get_field(self, index, field):
        """Gets the value of a field on a likeminded project.
        
        Considers the set of documents (LikeMinded project data) as an ordered
        list and finds the index-th document.  Returns the property of that 
        document given by field.
        """
        value = list(self.likeminded_data)[index].value[field]
        return value
    
    def get_document_key(self, ref_id):
        """Gets the unique identifying key for a given reference id.
        """
        for row in self.likeminded_data:
            if row.value['link'] == ref_id:
                return (row.value['name'], row.value['link'])

class CouchDataLoader (LikeMindedDataLoader):
    """Responsible for loading likeminded data from the Couch
    
    Requires the URL of the CouchDB server, and the name of the database.
    """
    
    def __init__(self, server, db):
        server = couchdb.Server(server)
        db = server[db]

        self.likeminded_data = db.query('function(doc) { emit(doc._id, doc); }')
    

class MySQLDataLoader (LikeMindedDataLoader):
    """Responsible for loading likeminded data from the Drupal MySQL database
    
    Requires the host name, database name, user name, and password.
    """
    
    def __init__(self, host, db, user, passwd):
        conn = mysqldb.connect(host=host,
                               user=user,
                               passwd=passwd,
                               db=db)
        
        cursor = conn.cursor()
        cursor.execute('''
            select nid,vid,title,
                field_process_value, 
                field_problem_value, 
                field_result_value 
            from node
                inner join field_data_field_process as process 
                    on node.nid = process.entity_id
                    and node.vid = process.revision_id
                inner join field_data_field_problem as problem
                    on node.nid = problem.entity_id
                    and node.vid = problem.revision_id
                inner join field_data_field_result as result
                    on node.nid = result.entity_id
                    and node.vid = result.revision_id
            where type='project';
        ''')
        
        # Make the mysql data look like the couch data.  Why?  Consistency, I
        # guess.
        
        class CouchImpersonator (object):
            def __init__(self, value):
                self.value = value
            
            def __repr__(self):
                return repr(self.value)
        
        self.likeminded_data = [
            CouchImpersonator({
             'link': str(nid),
             'name': name,
             'problem': problem,
             'process': process,
             'result': result})
            for (nid,vid,name,process,problem,result) in cursor]

def main(dl_type='mysql', ref_link=None, *args, **kwds):

    #Load in data from couch
    
    dl = LikeMindedDataLoaderFactory(dl_type, *args, **kwds)
    docs = dl.get_likeminded_data()
    all_posts = [post.lower().split() for post in docs]

    # Provides tf/idf/tf_idf abstractions for scoring

    tc = nltk.TextCollection(all_posts)

    # Compute a term-document matrix such that td_matrix[doc_title][term]
    # returns a tf-idf score for the term in the document

    td_matrix = {}
    for idx in range(len(all_posts)):
        post = all_posts[idx]
        fdist = nltk.FreqDist(post)

        doc_title = dl.get_field(idx, 'name')
        link = dl.get_field(idx, 'link')
        td_matrix[(doc_title, link)] = {}

        for term in fdist.iterkeys():
            td_matrix[(doc_title, link)][term] = tc.tf_idf(term, post)
    
    if ref_link is not None:
        ref_keys = [dl.get_document_key(ref_link)]
    else:
        ref_keys = td_matrix.keys()
    
    # Build vectors such that term scores are in the same positions...

    distances = {}
    for (title1, link1) in ref_keys:

        distances[(title1, link1)] = {}
        (max_score, most_similar) = (0.0, (None, None))

        for (title2, link2) in td_matrix.keys():

            # Take care not to mutate the original data structures
            # since we're in a loop and need the originals multiple times

            terms1 = td_matrix[(title1, link1)].copy()
            terms2 = td_matrix[(title2, link2)].copy()

            # Fill in "gaps" in each map so vectors of the same length can be 
            # computed

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

    # Print out a json object representing the distances.
    
    for ref_key in ref_keys:
        dists = []
        for rel_key in distances[ref_key]:
            dists.append({
                'reference_nid': ref_key[1],
                'related_nid': rel_key[1],
                'score': distances[ref_key][rel_key]
            })
        print json.dumps({'scores':dists})

def usage(err_code=0):
    print """Determine the textual distance between LikeMinded projects.

    $ likeminded_nlp.py DataLoaderType *Arguments [--ref=RefID]

Data loader types:
    mysql
    couch

MySQL arguments:
    host name
    database name
    username
    password

Couch arguments:
    server url
    database name

Examples:
    $ likeminded_nlp.py couch "http://localhost:5649" likeminded_projects
    $ likeminded_nlp.py mysql localhost catalyze username password --ref=623
    """
    exit(err_code)
    
if __name__ == '__main__':
    import sys
    import optparse
    
    parser = optparse.OptionParser()
    parser.add_option('--ref')
    (options,args) = parser.parse_args()
    
    if len(args) == 0:
        usage(1)
    
    dl_type = args[0]
    ref_link = options.ref
    
    if dl_type.lower() in ('mysql', 'drupal_mysql'):
        if len(args) != 5:
            usage(2)
        
        host = args[1]
        db = args[2]
        user = args[3]
        password = args[4]
        
        main(dl_type, ref_link, host, db, user, password)
    
    elif dl_type.lower() in ('couch'):
        if len(args) != 3:
            usage(3)
        
        server = args[1]
        db = args[2]
        
        main(dl_type, ref_link, server, db)
    
    else:
        usage()

