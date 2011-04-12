(function(){
  //lib wrapper for 3rd party modules
  var _lib = {
    util: require('util'),
    xml2js: require('xml2js'),
    request: require('request')
  },
  //options for querying likeminded
  _options = {
    lmBaseUrl: 'http://api.likeminded.org',
    lmApiKey: 'a084895b83fc9e1d9a1daa0d58e91a7e',
    couchBaseUrl: 'http://localhost:5984/likeminded'
  },
  //incrementer for the project page
  _projPage = 1,
  //total project pages to search in likeminded
  _totalProjPages,
  //total project count in likeminded
  _totalProjects;

  //xml2js project list parser
  var projListParser = new _lib.xml2js.Parser();
  //bind event handler when the xml parsing ends
  projListParser.addListener('end', function(json) {
    //console.log(_lib.util.inspect(json, false, 3));
    var i, showing = parseInt(json.results['@'].showing, 10);
    _totalProjects = parseInt(json.results['@'].available, 10);
    
    //loop over each project ide and then go get the project details
    for (i=0; i<showing; i++){
      getProjectDetails(json.results.project[i].id);
    }
    
    //calculate how many pages we need to search through if we haven't already done so
    if (!_totalProjPages) {
      _totalProjPages = Math.floor(_totalProjects / showing);
      if (_totalProjects % showing) {
        _totalProjPages++;
      }
    }

    //go get the next page if needed. recursion ftw!
    if (_projPage < _totalProjPages){
      _projPage++;
      getProjectList(_projPage);
    }
  });
  
  //xml2js project parser
  var projParser = new _lib.xml2js.Parser();
  //bind event handler when the xml parsing ends
  projParser.addListener('end', function(json) {
    //this is what we're going to put into couch
    var doc = {
      _id: json.id,
      likeminded: json
    };
    
    addToCouch(doc);
  });
  
  //go get the list of projects for the specified page, parse the xml, and handle with the 'end' event above  
  var getProjectList = function (page) {
    var url = _options.lmBaseUrl+'/search?apikey='+_options.lmApiKey+'&type=Project&page='+(page || 1);
    
    _lib.request({uri:url}, function (error, response, xml) {
      if (!error && response.statusCode === 200) {
        projListParser.parseString(xml);
      }
    });
  };

  //go get the project details for the specified id, parse the xml, and handle with the 'end' event above      
  var getProjectDetails = function (id) {
    var url = _options.lmBaseUrl+'/projects/'+id+'?apikey='+_options.lmApiKey;
    
    _lib.request({uri:url}, function (error, response, xml) {
      if (!error && response.statusCode === 200) {
        projParser.parseString(xml);
      }
    });  
  };
  
  //add a json object to couch
  var addToCouch = function(doc) {
    _lib.request({
        method: 'POST', 
        uri: _options.couchBaseUrl,
        headers: {
          'content-type': 'application/json'
        },
        body:JSON.stringify(doc)
    }, function (error, response, xml) {
      if (error) {
        console.log(error);
      }
    });  
  };

  //go get the first project page and go from there
  getProjectList(_projPage);
})();