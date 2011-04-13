"""
Object representations of the concepts in the likeminded API.
"""

import collections
import itertools

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



_Reference = collections.namedtuple('Reference', ['name', 'url', 'id'])
class BaseReference (_Reference):
    def __repr__(self):
        if not hasattr(self, 'type'):
            raise NotImplementedError(
                'Class %s must define a type attribute.' %
                self.__class__.__name__)
        
        return '%s%s' % (self.type, super(BaseReference, self).__repr__())
    
class ProjectReference (BaseReference):
    type = 'Project'

class ResourceReference (BaseReference):
    type = 'Resource'



ProjectDetails = collections.namedtuple('ProjectDetails', 
     ['id','name','status','start_date','end_date','problem','process','result',
     'external_feed_account_type','external_feed_account','locations','link',
     'resources','categories','created','updated'])
    
ResourceDetails = collections.namedtuple('ResourceDetails',
    ['id','name','description','url','created','updated','author','link',
     'locations','projects','categories'])



class CategoryList (tuple):
    @property
    def all(self):
        return self + self.subcategories
    @property
    def subcategories(self):
        return tuple(itertools.chain(*[category.subcategories for category in self]))

Category = collections.namedtuple('Category', ['id','name','subcategories'])

SubCategory = collections.namedtuple('SubCategory', ['id','name','category_id'])

Organization = collections.namedtuple('Organization', ['id','name'])

#
################################################################################

