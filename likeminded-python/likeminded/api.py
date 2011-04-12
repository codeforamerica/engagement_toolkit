"""
A wrapper on the LikeMinded REST API.
"""

from utils.xml2dict import xml2dict

from likeminded.connection import Connection

from likeminded.models import SearchResults
from likeminded.models import ProjectReference
from likeminded.models import ResourceReference

class Api (object):
    """The LikeMinded REST API wrapper.
    """
    def __init__(self, key=None, connection=None):
        self.__key = key
        self.__connection = connection or \
                            Connection('http://v1.api.likeminded.exygy.com')
    
    def search(self, query='', category=[], subcategory=[], 
               type='All', status='All', sort='All'):
        """
        Search resources or projects in Likeminded.
        
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
    
    def __search_helper(self, query, category, subcategory, 
                        type, status, sort, page):
        """
        A helper search function that is aware of pagination.  Pagination is
        abstracted out of the public search function so that the user has no
        need to be aware of it.
        """
        
        # Process the arguments.
        if isinstance(category, (list, tuple)):
            category = ','.join(category)
        if isinstance(subcategory, (list, tuple)):
            subcategory = ','.join(category) 
        
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

