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
    lmApiKey: 'YOUR-API-KEY',
    calaisBaseUrl: 'http://api.opencalais.com/tag/rs/enrich',
    calaisApiKey: 'YOUR-API-KEY',
    couchBaseUrl: 'http://localhost:5984/likeminded'
  },
  //incrementer for the project page
  _projPage = 1,
  //total project pages to search in likeminded
  _totalProjPages,
  //total project count in likeminded
  _totalProjects,
  //current project count, for debugging
  _curProjectCnt = 0;

  //start functions from opencalais for simplifying the json results
  //http://www.opencalais.com/documentation/calais-web-service-api/interpreting-api-response/opencalais-json-output-format
  function resolveReferences(flatdb) {
    for (var element in flatdb) {
      for (var attribute in flatdb[element]) {
        var val = flatdb[element][attribute];
        if (typeof val == 'string') {
          if (flatdb[val] != null) {
            flatdb[element][attribute] = flatdb[val];
          }
        }
      }
    }
  }
  
  function createHierarchy(flatdb) {
    var hdb = {};
    for (var element in flatdb) {
      var elementType = flatdb[element]._type;
      var elementGroup = flatdb[element]._typeGroup;
      if (elementGroup != null) {
        if (hdb[elementGroup] == null) {
          hdb[elementGroup] = {};
        }
        if (elementType != null) {
          if (hdb[elementGroup][elementType] == null) {
            hdb[elementGroup][elementType] = {};
          }
          hdb[elementGroup][elementType][element] = flatdb[element];
        } else {
          hdb[elementGroup][element] = flatdb[element];
        }
      } else {
        hdb[element] = flatdb[element];
      }
    }
    return hdb;
  }
  //end functions from opencalais for simplifying the json results

  //xml2js project list parser
  var projListParser = new _lib.xml2js.Parser();
  //bind event handler when the xml parsing ends
  projListParser.addListener('end', function(json) {
    //console.log(_lib.util.inspect(json, false, 3));
    var i, showing = parseInt(json.results['@'].showing, 10);
    _totalProjects = parseInt(json.results['@'].available, 10);
    
    //loop over each project ide and then go get the project details
    for (i=0; i<showing; i++){
      if (json.results.project[i] && json.results.project[i].id) {
        addProjectDetails(json.results.project[i].id);
      }
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
  projParser.addListener('end', function(doc) {
    _curProjectCnt++;
    
    console.log(_curProjectCnt + ' of ' + _totalProjects);
    
    addOpenCalaisDetails(doc);
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

  //go add the project details for the specified id, parse the xml, and handle with the 'end' event above      
  var addProjectDetails = function (id) {
    var url = _options.lmBaseUrl+'/projects/'+id+'?apikey='+_options.lmApiKey;
    
    _lib.request({uri:url}, function (error, response, xml) {
      if (!error && response.statusCode === 200) {
        projParser.parseString(xml);
      }
    });  
  };
  
  //Go add the OpenCalais details based on the text from likeminded
  var addOpenCalaisDetails = function (doc) {
    var text = doc.name + ' ' +
      doc.problem + ' ' + 
      doc.process + ' ' + 
      doc.result;
    
    _lib.request({
        method: 'POST', 
        uri: _options.calaisBaseUrl,
        headers: {
          'X-Calais-Licenseid': _options.calaisApiKey,
          'content-type': 'text/raw',
          'Outputformat': 'Application/JSON'
        },
        body: text
    }, function (error, response, jsonStr) {
      var jsonObj, simpleJson;
      if (!error && response.statusCode === 200) {
        jsonObj = JSON.parse(jsonStr);
        
        resolveReferences(jsonObj);
        simpleJson = createHierarchy(jsonObj);
        
        doc.opencalais = simpleJson;
        addToCouch(doc);
      } else {
        console.log(jsonStr);
        console.log('Error parsing OpenCalais response for Project ' + doc.id);
        
        //retry logic because OpenCalais only allows 4 queries per second
        setTimeout(function() {
          addOpenCalaisDetails(doc);
        }, 1000);
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
        console.log('Error adding Project ' + doc._id + ' to couch.');
      }
    });  
  };

  //go get the first project page and go from there
  getProjectList(_projPage);
})();