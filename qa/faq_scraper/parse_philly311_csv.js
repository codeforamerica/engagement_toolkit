(function(){
  var fs = require('fs'),
      path = require('path'),
      request = require('request'),
      semhack = require('./semantic_hacker.js'),
      options = {
        semanticHackerApiKey: 'YOUR API KEY'
      };

  //Parse a single line of a file
  var parseLine = function(line, headers) {
    //NOTE: this leave extra double-quotes on the first and last value
    var values = line.split('","'),
        url, date, id, match,
        parsedLines = [],
        data = {};
    
    headers.forEach(function(header, c) {
      data[header] = strip(values[c]).replace(/\s+/g, ' ');
    });
        
    return data;
  };
  
  //Convert a record to CSV
  var toCsv = function(data) {
    var csv = '"url","createDate","questionNumber","question","answer","tags"\n';
    data.forEach(function(rec, i) {
      csv += '"' + rec.url + '","' + rec.createDate + '","' + 
          rec.questionNumber + '","' + rec.question + '","' + rec.answer + '","' + rec.tags.join(';') + '"\n'; 
    });
    
    return csv;
  };
  
  //Remove dupes if the question and answer are identical
  var dedupe = function(data) {
    var i, prevRec, curRec, dedupedData = [];
    
    //Sort everything by questions/answer
    data.sort(function(a, b) {
      if (a.question === b.question) {
        if (a.answer === b.answer) {
          return 0;
        } else {
          return a.answer < b.answer ? -1 : 1;
        }
      } else {
        return a.question < b.question ? -1 : 1;
      }
    });
    
    //De-dupe
    if (data.length > 0) {
      dedupedData.push(data[0]);
    
      for (i=1; i<data.length; i++) {
        prevRec = data[i-1];
        curRec = data[i];
        
        //Only add the record if it's different than the
        //previous record.
        if (curRec.question !== prevRec.question ||
            curRec.answer !== prevRec.answer) {
          dedupedData.push(data[i]);
        }
      }
    }
    
    return dedupedData;
  };

  //Go get tags from SemanticHacker for our QA
  var addTags = function(data, throttle, callback) {
    var c, taggedData = [];
    
    if (data.length > 0) {
      data.forEach(function(rec, c) {
        //Fancy closure to keep access to the text inside the query call
        (function(text) {
          //SemanticHacker throttles you to 300 requests per minutes,
          //so this code will slow that down
          setTimeout(function(){
            semhack.getTags({apiKey: options.semanticHackerApiKey}, text, function(tagsObj){
              var tags = [],
                  i;

              for(i=0; i<tagsObj.length; i++) {
                tags.push(tagsObj[i].label);
              }
              
              //Always add tags, even if blank
              data[c].tags = tags;

              taggedData.push(data[c]);

              console.log(taggedData.length + ' of ' + data.length);
              
              //Callback once the tagged data is the same size as the
              //original data
              if (data.length === taggedData.length) {
                console.log(data.length + ' records! Writing file.');
                callback(taggedData);
              }
            });
          }, (c * throttle));

        })(rec.question + ' ' + rec.answer + ' ' + rec.url); //This is the text var up above
      });
    } else {
      callback(taggedData);
    }
  };
  
  //Helper function to remove double quotes
  var strip = function(str) {
    return str ? str.replace(/"\r*/, '').trim() : '';
  };
  
  //Parse a single file into an array of structured data
  var parseFile = function(inputFile) {
    var fileStr,
        headers,
        lines,
        parsedData = [],
        i;
    
    if (inputFile) {      
      fileStr = fs.readFileSync(inputFile).toString();
      //Clean up all of the cells that contain line breaks
      fileStr = fileStr.replace(/([^"])(\r\n)+/g, '$1 ');

      lines = fileStr.split('\n');
      
      //NOTE: this leave extra double-quotes on the first and last value
      headers = lines[0].split('","');
      headers[0] = strip(headers[0]);
      headers[headers.length-1] = strip(headers[headers.length-1]);

      for (i=1; i<lines.length; i++) {
        //parseLine can return a dataObject or an array of dataObjects.
        //concat is smart enough to handle either.
        parsedData = parsedData.concat(parseLine(lines[i], headers));
      }
    } else {
      console.log('No input was specified.');
    }
    
    return parsedData;
  };
  
  //Function to synchronously process a list of files
  var processFiles = function(filePaths, outputDir) {
    var parsedData,
        fileName = filePaths.pop();

    if (fileName && fileName.indexOf('.csv') !== -1) {
      //Parse the file
      parsedData = dedupe(parseFile(fileName));

      //Add tags to the file from SemanticHacker
      addTags(parsedData, 250, function(taggedData) {
        //Write the file
        fs.writeFile(path.join(outputDir, path.basename(fileName)), toCsv(taggedData));
        
        //Go to the next file, if any
        if (filePaths.length > 0) {
          processFiles(filePaths, outputDir);
        }
      });
    } else {
      //Go to the next file, if any
      if (filePaths.length > 0) {
        processFiles(filePaths, outputDir);
      }
    }
  };
  
  //Init
  (function() {
    var input = process.argv[2],
        output = process.argv[3],
        filePaths = [],
        i;
    
    path.exists(input, function (exists) {
      var parsedFileData;
      
      if (exists) {
        fs.readdir(input, function(error, files) {
          //Process a single file
          if (error && error.code === 'ENOTDIR') {
            filePaths.unshift(input);
            processFiles(filePaths, output);
          } else {
            //Process a directory of files
            for (i=0; i<files.length; i++) {
              filePaths.unshift(path.join(input, files[i]));
            }
            processFiles(filePaths, output);
          }
        });
      } else {
        console.log(input + ' does not exist.');
      }
    });
  })();
})();
