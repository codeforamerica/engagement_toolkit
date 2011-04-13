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
            elif data['category'] == '1':
                content = const.SEARCH_RESULTS_CATEGORY_ARTS
            
            response = None
            return response, content
        
        self.conn = conn
    
    def test_ShouldAcceptMultipleTypesForcategory(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        categories = [1, '1', [1], ['1']]
        
        for category in categories:
            self.assertEqual(len(api.search(category=category)), 117)
    
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
        
        @patch(conn)
        def post(self, path, data={}):
            content = data['project']
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_ExpectedProjectIsCreated(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        project = api.create_project(name='Hello, world!', process='We just did it')
        
        self.assertEqual(project.__class__.__name__, 'ProjectDetails')
        self.assertEqual(project.name, 'Hello, world!')
        self.assertEqual(project.process, 'We just did it')
        self.assertEqual(project.end_date, None)
        
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
            self.assertEquals(project._asdict()[key], value)


class TestLikeMindedResource (unittest.TestCase):
    
    def setUp(self):
        from likeminded.connection import Connection
        conn = Connection('mylikemindedserver', http='No HTTP')
        
        import re
        exp = re.compile(r'^.*/resources/(?P<resource_id>\d+)$')
        
        @patch(conn)
        def get(self, path, data={}):
            match = exp.match(path)
            project_id = match.group('resource_id')
            
            if project_id == '200':
                content = const.RESOURCE_200
            
            response = None
            return response, content
        
        @patch(conn)
        def post(self, path, data={}):
            content = data['resource']
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_ExpectedResourceIsCreated(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        resource = api.create_resource(name='Hello, world!', description='Stuff we have')
        
        self.assertEqual(resource.__class__.__name__, 'ResourceDetails')
        self.assertEqual(resource.name, 'Hello, world!')
        self.assertEqual(resource.description, 'Stuff we have')
        self.assertEqual(resource.url, None)
        
    def test_ProjectReferenceIsAsExpected(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        resource = api.read_resource('200')
        
        expected_res = {
            'id' : '200',
            'name' : 'Gaining Ground: Supporting English Learners Through After-School Literacy Programming',
            'created' : '2011-01-21 19:30:30',
            'updated' : '2011-01-21 19:30:30',
            'url' : 'http://www.issuelab.org/data_partners/likeminded/gaining_ground_supporting_english_learners_through_after_school_literacy_programming',
            'link' : 'http://likeminded.exygy.com/resource/gaining-ground-supporting-english-learners-through-after-school-literacy-programming',
            'locations' : None,
        }
        
        for (key, value) in expected_res.items():
            self.assertEquals(resource._asdict()[key], value)



class TestLikeMindedCategories (unittest.TestCase):
    
    def setUp(self):
        from likeminded.connection import Connection
        conn = Connection('mylikemindedserver', http='No HTTP')
        
        @patch(conn)
        def get(self, path, data={}):
            if path == '/categories':
                content = const.CATEGORIES
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_TheRightNumberOfCategoriesAndSubcategoriesAreReturned(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        categories = api.categories()
        self.assertEquals(len(categories.all), 51)
        
    def test_TheRightNumberOfCategoriesAreReturned(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        categories = api.categories()
        self.assertEquals(len(categories), 8)
        
    def test_TheRightNumberOfSubCategoriesAreReturned(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        subcategories = api.categories()
        self.assertEquals(len(subcategories.subcategories), 43)


class TestLikeMindedOrganizations (unittest.TestCase):
    
    def setUp(self):
        from likeminded.connection import Connection
        conn = Connection('mylikemindedserver', http='No HTTP')
        
        @patch(conn)
        def get(self, path, data={}):
            if path == '/organizations':
                content = const.ORGANIZATIONS
            
            response = None
            return response, content
        
        self.conn = conn
        
    def test_TheRightNumberOfOrganizationsAreReturned(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        orgs = api.organizations()
        self.assertEquals(len(orgs), 786)
        
    def test_AllThingsReturnedAreOrganizations(self):
        api = likeminded.Api(key='', connection=self.conn)
        
        orgs = api.organizations()
        for org in orgs:
            self.assertEqual(org.__class__.__name__, 'Organization')
