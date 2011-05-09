var fs = require('fs'),
    path = require('path'),
    util = require('util'),
    request = require('request');

exports.getTags = function(options, text, callback) {
  var uri = 'http://api.semantichacker.com/{YOUR_API_KEY}/concept?format=json'
            .replace('{YOUR_API_KEY}', options.apiKey);
  
  request({
      method: 'POST', 
      uri: uri,
      body: text
  }, function (error, response, jsonStr) {
    var jsonObj,
        tags;

    if (!error && response.statusCode === 200) {
      jsonObj = JSON.parse(jsonStr);

      //Extract the tags from the response
      if (jsonObj.conceptExtractor && jsonObj.conceptExtractor.conceptExtractorResponse) {
        tags = jsonObj.conceptExtractor.conceptExtractorResponse.concepts;
      } else {
        //We'll see an error here if we go faster than 300 req/min
        throw new Error('SemanticHacker error: ' + util.inspect(jsonObj));
      }

      callback(tags);
    } else {
      throw new Error('Failed to get a response from SemanticHacker: ' + util.inspect(error));
    }
  });
};