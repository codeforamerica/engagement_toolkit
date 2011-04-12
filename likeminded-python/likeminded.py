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
    def __init__(self, available=0, references=[], inc_page=None):
        self.__available = available
        self.__inc_page = inc_page
        self.__references = references
    
    def __len__(self):
        return self.__available
    
    def __iter__(self):
        if len(self.__references) == 0:
            raise StopIteration
        
        for reference in self.__references:
            yield reference
        
        next_results = self.__inc_page(1)
        
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
    
    def search(self, query=None, page=1):
        """
        Search resources or projects in Likeminded.
        Return a ``likeminded.SearchResults`` object.
        """
        search_terms = { 'query' : query, 'page' : page }
        search_xml = self.__connection.get('/search/', search_terms)
        
        search_dict = xml2dict(search_xml)
        results_dict = search_dict.search_results.results
        
        results = self.__make_search_results(
            results_dict, 
            lambda inc_pg: self.search(query=query, page=page+inc_pg))
        return results
    
    def __make_search_results(self, results_dict, inc_page, ResultsClass=SearchResults):
        projects = self.__make_references(results_dict.get('project', []))
        resources = self.__make_references(results_dict.get('resource', []))
        
        results = SearchResults(
            available=int(results_dict.available),
            references=projects + resources,
            inc_page=inc_page
        )
        
        return results
    
    def __make_references(self, ref_list, RefClass=Reference):
        if not isinstance(ref_list, list):
            ref_list = [ref_list]
        
        references = []
        for ref_dict in ref_list:
            reference = RefClass(name=ref_dict.name, 
                                 url=ref_dict.likeminded_url,
                                 id=ref_dict.id)
            references.append(reference)
        
        return references

