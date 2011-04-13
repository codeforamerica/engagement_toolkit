"""Python wrapper for the LikeMinded REST API.

>>> api = Api(key='abc123mykey')
>>> categories = api.categories()
>>> for category in categories:
...   print category.id, category.name
... 
1 Arts
2 Health
3 Education
4 Crime & Safety
5 Environment
6 Economy
7 Government
8 Community
>>>
>>> references = api.search(category=1)
>>> len(references)
117
>>> for reference in references:
...   print reference.type, reference.id, reference.name
... 
Project 138 Unified Theater empowers children with disabilities
Project 143 Bringing the Arts Community Together to Save School Music Programs
Project 153 How Skateboarders Saved a Park
Project 155 Instilling hope in North Philadelphia through the arts
.
.
.
>>>
"""

from likeminded.connection import Connection

from likeminded.models import SearchResults
from likeminded.models import ProjectReference
from likeminded.models import ResourceReference
from likeminded.models import ProjectDetails
from likeminded.models import ResourceDetails
from likeminded.models import CategoryList
from likeminded.models import Category
from likeminded.models import SubCategory
from likeminded.models import Organization

from likeminded.utils.xml2dict import dict2xml
from likeminded.utils.xml2dict import xml2dict

class Api (object):
    """The LikeMinded REST API wrapper.
    
    >>> import likeminded
    >>> api = likeminded.Api(key='abc123mykey')
    
    >>> categories = api.categories()
    >>>
    >>> references = api.search(
    """
    
    def __init__(self, key=None, connection=None):
        self.__key = key
        self.__connection = connection or \
                            Connection('http://v1.api.likeminded.exygy.com')
    
    def search(self, query='', category=[], subcategory=[], 
               type='All', status='All', sort='All'):
        """Search resources or projects in Likeminded.
        
        Keyword arguments:
        category -- A list of 
        
        Return a ``SearchResults`` object.  This object behaves kind of like a
        list, except that it doesn't support indexing.  You can check the number
        of objects it contains with ``len(results)``, and iterate through it 
        with ``for reference in results: ...``.
        
        The objects contained in the ``SearchResults`` object are references
        to projects and resources.  They have four attributes: ``name``, 
        ``type``, ``url``, and ``id``.
        """
        return self.__search_helper(query, category, subcategory, 
                                    type, status, sort, 1)
    
    def read_project(self, id):
        """Read a project from LikeMinded.
        
        Arguments:
        id -- The project id as a string or an integer
        
        Return a ProjectDetails object.
        """
        path = '/projects/%s' % id
        query = { 'apikey' : self.__key }
        response, detail_xml = self.__connection.get(path, query)
        
        return self.__read_details_helper(detail_xml, 'project', ProjectDetails)
    
    def read_resource(self, id):
        """Read a resource from LikeMinded.
        
        Arguments:
        id -- The resource id as a string or an integer
        
        Return a ResourceDetails object.
        """
        path = '/resources/%s' % id
        query = { 'apikey' : self.__key }
        response, detail_xml = self.__connection.get(path, query)
        
        return self.__read_details_helper(detail_xml, 'resource', ResourceDetails)
    
    def create_project(self, **kwds):
        """Write a new project to LikeMinded.
        
        Return a ProjectDetails object representing the newly created data.
        """
        project_xml = dict2xml({'project':kwds})
        
        path = '/projects'
        query = { 'apikey' : self.__key,
                  'project' : project_xml }
        response, project_xml = self.__connection.post(path, query)
        
        return self.__read_details_helper(project_xml, 'project', ProjectDetails)
    
    def create_resource(self, **kwds):
        """Write a new resource to LikeMinded.
        
        Return a ResourceDetails object representing the newly created data.
        """
        resource_xml = dict2xml({'resource':kwds})
        
        path = '/resources'
        query = { 'apikey' : self.__key,
                  'resource' : resource_xml }
        response, resource_xml = self.__connection.post(path, query)
        
        return self.__read_details_helper(resource_xml, 'resource', ResourceDetails)
    
    def categories(self):
        """Get all categories and subcategories used in LikeMinded.
        
        Return a CategoryList object.  This is like a tuple of Category objects.
        It has two additional properties: ``subcategories``, which returns a
        list of all Subcategory objects, and ``all``, which gives all 
        Category and Subcategory objects.
        """
        path = '/categories'
        query = { 'apikey' : self.__key }
        response, categories_xml = self.__connection.get(path, query)
        
        category_list = []
        categories_dict = xml2dict(categories_xml).categories
        
        subcategories_by_category_id = {}
        for subcategory_dict in categories_dict.sub_categories:
            subcategory = SubCategory(**subcategory_dict)
            
            cid = subcategory.category_id
            if cid not in subcategories_by_category_id:
                subcategories_by_category_id[cid] = [subcategory]
            else:
                subcategories_by_category_id[cid].append(subcategory)
        
        categories_by_id = {}
        for category_dict in categories_dict.category:
            category_dict['subcategories'] = \
                subcategories_by_category_id[category_dict.id]
            category = Category(**category_dict)
            
            categories_by_id[category.id] = category
            category_list.append(category)
        
        categories = CategoryList(category_list)
        
        return categories
    
    def organizations(self):
        """Get all the organizations used in LikeMinded.
        
        Return a list of Organization objects.
        """
        path = '/organizations'
        query = { 'apikey' : self.__key }
        response, organizations_xml = self.__connection.get(path, query)
        
        organizations = []
        organizations_dict = xml2dict(organizations_xml).organizations
        
        for organization_dict in organizations_dict.organization:
            organization = Organization(**organization_dict)
            organizations.append(organization)
        
        return organizations
    
    def __search_helper(self, query, category, subcategory, 
                        type, status, sort, page):
        """
        A helper search function that is aware of pagination.  Pagination is
        abstracted out of the public search function so that the user has no
        need to be aware of it.
        """
        
        # Process the arguments.
        if isinstance(category, (list, tuple)):
            category = ','.join(map(str, category))
        else:
            category = str(category)
        
        if isinstance(subcategory, (list, tuple)):
            subcategory = ','.join(map(str, subcategory)) 
        else:
            subcategory = str(subcategory)
        
        search_terms = { 'query' : query,
                         'category' : category, 
                         'subcategory' : subcategory, 
                         'type' : type, 
                         'status' : status, 
                         'sort' : sort,
                         'page' : page, 
                         'apikey' : self.__key }
        response, search_xml = self.__connection.get('/search/', search_terms)
        
        search_dict = xml2dict(search_xml)
        results_dict = search_dict.search_results.results
        
        results = self.__make_search_results(
            results_dict, 
            lambda: self.__search_helper(query, category, subcategory, 
                                         type, status, sort, page+1))
        return results
    
    def __make_search_results(self, results_dict, next_page, 
                              ResultsClass=SearchResults):
        """
        The SearchResults factory function
        """
        projects = self.__make_references(results_dict.get('project', []), 
                                          ProjectReference)
        resources = self.__make_references(results_dict.get('resource', []), 
                                           ResourceReference)
        
        results = SearchResults(
            available=int(results_dict.available),
            references=projects + resources,
            next_page=next_page
        )
        
        return results
    
    def __make_references(self, ref_list, RefClass):
        """
        A factory method that creates a list of Reference objects.
        """
        if not isinstance(ref_list, list):
            ref_list = [ref_list]
        
        references = []
        for ref_dict in ref_list:
            reference = RefClass(name=ref_dict.name, 
                                 url=ref_dict.likeminded_url,
                                 id=ref_dict.id)
            references.append(reference)
        
        return references
    
    def __read_details_helper(self, detail_xml, type_string, DetailClass):
        """
        Use this method to read the details responses from get and post 
        requests for LikeMinded projects and resources.
        """
        detail_dict = xml2dict(detail_xml)[type_string]
        detail_dict = self.__fill_in_params(detail_dict, DetailClass)
        details = DetailClass(**detail_dict)
        return details
    
    def __fill_in_params(self, params_dict, ForClass):
        """
        Fill in any missing parameters from the fields of the given class.
        """
        if not hasattr(ForClass, '_fields'):
            raise ValueError(
                "Can't access the fields of class %r; " % ForClass.__name__ + \
                "please use a 'namedtuple'.")
        
        for key in ForClass._fields:
            if key not in params_dict:
                params_dict[key] = None
        
        return params_dict

