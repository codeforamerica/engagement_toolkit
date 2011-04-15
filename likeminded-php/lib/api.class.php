<?php

require 'connection.class.php';
class Api {
	
	private $_key, $_connection;
	
	public function __construct($key, $connection = false) {
		$this->_key = $key;
		$this->_connection = ($connection) ? $connection : new Connection('http://v1.api.likeminded.exygy.com');
	}
	
	public function search($query='', $category=false, $subcategory=false, $type='All', $status='All', $sort='All') {
		/*
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
        */
        return $this->_search_helper($query, $category, $subcategory, $type, $status, $sort, 1);
	}
	
	private function _search_helper($query, $category, $subcategory, $type, $status, $sort, $page) {
        /*
        A helper search function that is aware of pagination.  Pagination is
        abstracted out of the public search function so that the user has no
        need to be aware of it.
        */
        
        # Process the arguments.
		$category = (is_array($category)) ? implode(',', $category) : strval($category);
        
		$subcategory = (is_array($subcategory)) ? implode(',', $subcategory) : strval($subcategory);
        
        $search_terms = array('query' => $query,
                         'category' => $category, 
                         'subcategory' => $subcategory, 
                         'type' => $type, 
                         'status' => $status, 
                         'sort' => $sort,
                         'page' => $page, 
                         'apikey' => $this->_key);

		$search_xml = $this->_connection->get('/search/', $search_terms);
		return $search_xml;
		
        /*
       	 search_dict = xml2dict(search_xml)
	        results_dict = search_dict.search_results.results

	        results = self.__make_search_results(
	            results_dict, 
	            lambda: self.__search_helper(query, category, subcategory, 
	                                         type, status, sort, page+1))
	        return results
		*/
	
	}
}
?>