"""
Tests for the likeminded wrapper module.
"""

import unittest
import tests.strings_fortesting as const
from utils.testing import patch

import likeminded

class TestLikeMindedSearchResults (unittest.TestCase):
    
    def setUp(self):
        from likeminded.connection import Connection
        conn = Connection('mylikemindedserver', http='No HTTP')
        
        @patch(conn)
        def get(self, path, data={}):
            if data['query'] == 'school':
                content = const.SEARCH_RESULTS_1
            elif data['query'] == 'ishkabibble':
                content = const.SEARCH_RESULTS_2
            elif data['query'] == 'high school' and data['page'] == 1:
                content = const.SEARCH_RESULTS_HIGH_SCHOOL_PG_1
            elif data['query'] == 'high school' and data['page'] == 2:
                content = const.SEARCH_RESULTS_HIGH_SCHOOL_PG_2
            elif data['query'] == 'high school' and data['page'] == 3:
                content = const.SEARCH_RESULTS_HIGH_SCHOOL_PG_3
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_SearchResultsLengthShouldBeAsExected(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        searches = [
            [(), {'query' : 'school'}, 1121],
            [(), {'query' : 'ishkabibble'}, 0],
        ]
        
        for (params, kwds, result) in searches:
            self.assertEqual(len(api.search(*params, **kwds)), result)
    
    def test_CanIterateThoughAllSearchResults(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        results = api.search(query='high school')
        cnt = 0
        for reference in results:
            cnt += 1
        
        self.assertEquals(cnt, 11)
    
    def test_ProjectReferenceIsAsExpected(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        results = api.search(query='school')
        project_ref = iter(results).next()
        
        expected_ref = {
            'id' : '137',
            'name' : 'Tackling the achievement gap with a math competition',
            'url' : 'likeminded.exygy.com/projects/tackling-the-achievement-gap-with-a-math-competition'
        }
        
        self.assertEquals(project_ref.__class__.__name__, 'ProjectReference')
        self.assertEquals(project_ref._asdict(), expected_ref)
    
    def test_ResourceReferenceIsAsExpected(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        results = api.search(query='school')
        results_iter = iter(results)
        results_iter.next()
        results_iter.next()
        resource_ref = results_iter.next()
        
        expected_ref = {
            'id' : '1740',
            'name' : 'Links to Learning and Sustainability: Year Three Report of the Pennsylvania High School Coaching Initiative',
            'url' : 'likeminded.exygy.com/resources/links-to-learning-and-sustainability-year-three-report-of-the-pennsylvania-high-school-coaching-init'
        }
        
        self.assertEquals(resource_ref.__class__.__name__, 'ResourceReference')
        self.assertEquals(resource_ref._asdict(), expected_ref)



class TestLikeMindedProject (unittest.TestCase):
    
    def setUp(self):
        from likeminded.connection import Connection
        conn = Connection('mylikemindedserver', http='No HTTP')
        
        import re
        
        exp = re.compile(r'^.*/projects/(?P<project_id>\d+)$')
        
        @patch(conn)
        def get(self, path, data={}):
            match = exp.match(path)
            project_id = match.group('project_id')
            
            if project_id == '193':
                content = const.PROJECT_193
            elif project_id == '124':
                content = const.PROJECT_124
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_ProjectReferenceIsAsExpected(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        project = api.read_project('193')
        
        expected_proj = {
            'id' : '193',
            'name' : 'Saving for Education',
            'status' : '2',
            'start_date' : None,
            'end_date' : None,
            'created' : '2011-03-14 20:45:26',
            'updated' : '2011-03-17 15:07:42',
            'external_feed_account' : None,
            'link' : 'http://likeminded.exygy.com/project/saving-for-education',
        }
        
        for (key, value) in expected_proj.items():
            self.assertEquals(project._asdict().get(key), value)

