"""
Object representations of the concepts in the likeminded API.
"""

################################################################################
# You probably shouldn't be creating the objects below directly ever.  Use the
# methods in the Api class to generate instances of these classes instead.  See
# the likeminded.api module.
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

