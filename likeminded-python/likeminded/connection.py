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
    
    def __request(self, path, method, query=None, body=None, headers=None):
        url = '%s/%s' % (self.__root, path)
        
        # URL encode any available query data
        if query:
            query = urllib.urlencode(query)
        
        # Add urlencoded data to the path as a query if method is GET or DELETE
        if method.lower() in ('get', 'delete') or body is not None:
            if query:
                path = '%s?%s' % (path, query)
        
        # If method is POST or PUT, and the body is None, put the query data
        # into the body
        else:
            body = query
        
        url='%s/%s' % (self.__root, path)
        return self.__http.request(url, method, body, headers)
    
    def get(self, path, data={}):
        return self.__request(path, 'GET', data)
    
    def post(self, path, data={}, body=None):
        return self.__request(path, 'POST', data, body)
        
    def put(self, path, data={}, body=None):
        return self.__request(path, 'PUT', data, body)
    
    def delete(self, path, data={}):
        return self.__request(path, 'DELETE', data)

