"""
A structure to manage the HTTP connection between a LikeMinded REST server and
the rest of the library.
"""

import httplib2
import urllib

class Connection (object):
    """
    Handle calls to the LikeMinded server.
    """
    def __init__(self, server, http=None):
        self.__http = http or httplib2.Http()
        self.__root = server
    
    def __request(self, path, method, data=None, headers=None):
        url = '%s/%s' % (self.__root, path)
        
        # URL encode any available data
        if data:
            query = urllib.urlencode(data)
        
        # Add urlencoded data to the path as a query if method is GET or DELETE
        if method.lower() in ('get', 'delete'):
            path = path if not data else '%s?%s' % (path, query)
            body = None
        
        # If method is POST or PUT, put the query data into the body
        else:
            body = None if not data else query
        
        url='%s/%s' % (self.__root, path)
        return self.__http.request(url, method, body, headers)
    
    def get(self, path, data={}):
        return self.__request(path, 'GET', data)
    
    def post(self, path, data={}):
        return self.__request(path, 'POST', data)
        
    def put(self, path, data={}):
        return self.__request(path, 'PUT', data)
    
    def delete(self, path, data={}):
        return self.__request(path, 'DELETE', data)

