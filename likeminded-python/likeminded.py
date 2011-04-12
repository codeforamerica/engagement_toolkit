"""
A wrapper on the LikeMinded REST API.
"""

import httplib
from utils.xml2dict import xml2dict

class Connection (object):
    """
    Handle calls to the LikeMinded server.
    """
    def get(self, path, data={}):
        pass

################################################################################
# You probably shouldn't be creating the objects below directly ever.  Use the
# methods in the Api class to generate instances of these classes instead.  See
# toward the bottom on this module.
#

class SearchResults (object):
    def __init__(self, available=0, references=[], next_page=None):
        """Create a SearchResults object.
        
        Keyword arguments:
        available -- The total number of references available in the results
        references -- The initial list of references available on the first page
        next_page -- A function that will return the results for the next page
        
        """
        self.__available = available
        self.__next_page = next_page
        self.__references = references
    
    def __len__(self):
        """
        Count the number of available references in the search results.
        """
        return self.__available
    
    def __iter__(self):
        """
        Iterate through the project and resource references in the search 
        results.
        """
        if len(self.__references) == 0:
            raise StopIteration
        
        # First go through all the references on this results object's page
        for reference in self.__references:
            yield reference
        
        # Then, get the results object for the next page and iterate through it
        next_results = self.__next_page()
        for reference in next_results:
            yield reference

class Reference (object):
    type = None
    def __init__(self, name='', url='', id=''):
        self.name = name
        self.url = url
        self.id = id
    
class ProjectReference (Reference):
    type = 'project'

class ResourceReference (Reference):
    type = 'resource'

#
################################################################################

class Api (object):
    """
    The actual API wrapper class.  In most cases, all use of this module will
    begin through this class.
    """
    def __init__(self, key=None, connection=None):
        self.__connection = connection
    
    def search(self, query=None):
        """
        Search resources or projects in Likeminded.
        Return a ``likeminded.SearchResults`` object.
        """
        return self.__search_helper(query, 1)
    
    def __search_helper(self, query, page):
        """
        A helper search function that is aware of pagination.  Pagination is
        abstracted out of the public search function so that the user has no
        need to be aware of it.
        """
        search_terms = { 'query' : query, 'page' : page }
        search_xml = self.__connection.get('/search/', search_terms)
        
        search_dict = xml2dict(search_xml)
        results_dict = search_dict.search_results.results
        
        results = self.__make_search_results(
            results_dict, 
            lambda: self.__search_helper(query, page+1))
        return results
    
    def __make_search_results(self, results_dict, next_page, ResultsClass=SearchResults):
        """
        The SearchResults factory function
        """
        projects = self.__make_references(results_dict.get('project', [], ProjectReference))
        resources = self.__make_references(results_dict.get('resource', [], ResourceReference))
        
        results = SearchResults(
            available=int(results_dict.available),
            references=projects + resources,
            next_page=next_page
        )
        
        return results
    
    def __make_references(self, ref_list, RefClass=Reference):
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

