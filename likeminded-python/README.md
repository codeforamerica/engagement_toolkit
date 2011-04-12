likeminded-python
=================
A Python wrapper around the LikeMinded API.

Usage Examples
--------------
    import likeminded
    
    api = likeminded.Api(key='yourapikey')
    
    # Search resources and projects
    results = api.search(query='search term')
    
    # Iterate through search results
    for reference in results:
        print reference

Copyright
---------
Copyright (c) 2010 Code for America Laboratories
See [LICENSE](https://github.com/cfalabs/open311/blob/master/LICENSE.mkd) for details.
