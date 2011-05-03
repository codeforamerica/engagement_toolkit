(function(){
  var fs = require('fs'),
      path = require('path');

  var parseLine = function(line, headers) {
    //NOTE: this leave extra double-quotes on the first and last value
    var values = line.split('","'),
        url, date, id, match,
        parsedLines = [],
        data = {
          properties: {},
          questions: {},
          answers: {}
        };
    
    headers.forEach(function(header, c) {
      val = strip(values[c]).replace(/\s+/g, ' ');
                
      if (val) {
        match = /(\d+)/.exec(header);
        
        //Is this a Question or Answer?
        if (header.indexOf('Answer') !== -1 && match) {
          id = match[1];
          
          if (header.indexOf('Q') !== -1) {
            //If this is an question, parse out the question number from the key 
            //and save the value
            data.questions[id] = val;
          } else {
            //If this is an answer, parse out the answer number from the key and 
            //save the value
            data.answers[id] = val;
          } 
        } else {
          //These are other properties of the question
          data.properties[header] = val;        
        }
      }
    });
    
    url = data.properties['Input.url'];
    date = data.properties['CreationTime'];
    
    for (key in data.questions) {
      parsedLines.push({
        "url": url,
        "createDate": date,
        "questionNumber": key,
        "question": data.questions[key],
        "answer": data.answers[key]
      });
    }
    
    return parsedLines;
  };
  
  var toCsv = function(data) {
    var csv = '"url","createDate","questionNumber","question","answer"\n';
    data.forEach(function(rec, i) {
      csv += '"' + rec.url + '","' + rec.createDate + '","' + 
          rec.questionNumber + '","' + rec.question + '","' + rec.answer + '"\n'; 
    });
    
    return csv;
  };
  
  var dedupe = function(parsedData) {
    var i, prevRec, curRec, dedupedData = [];
    
    parsedData.sort(function(a, b) {
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
    if (parsedData.length > 0) {
      dedupedData.push(parsedData[0]);
    
      for (i=1; i<parsedData.length; i++) {
        prevRec = parsedData[i-1];
        curRec = parsedData[i];
        
        //Is this a dupe
        if (curRec.question !== prevRec.question ||
            curRec.answer !== prevRec.answer) {
          dedupedData.push(parsedData[i]);
        }
      }
    }
    
    return dedupedData;
  };
  
  var strip = function(str) {
    return str ? str.replace(/"\r*/, '').trim() : '';
  };
  
  var parseFile = function(inputFile, outputDir) {
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
        parsedData = parsedData.concat(parseLine(lines[i], headers));
      }
    } else {
      console.log('Usage: node parse_mt_csv.js turk_file_to_parse.csv');
    }
    
    return parsedData;
  };
  
  //Init
  (function() {
    var input = process.argv[2],
        outputDir = process.argv[3];
    
    path.exists(input, function (exists) {
      if (exists) {
        fs.readdir(input, function(errors, files) {
          var parsedAllFilesData = [];
          
          files.forEach(function(file) {
            var parsedFileData;
                        
            if (file.indexOf('.csv') !== -1) {
              parsedFileData = dedupe(parseFile(path.join(input, file), outputDir));
              parsedAllFilesData = parsedAllFilesData.concat(parsedFileData);
              
              console.log(path.join(outputDir, path.basename(file)));
              fs.writeFile(path.join(outputDir, path.basename(file)), toCsv(parsedFileData));
            }
          });
          
          console.log(path.join(outputDir, 'merged.csv'));
          fs.writeFile(path.join(outputDir, 'merged.csv'), toCsv(dedupe(parsedAllFilesData)));          
        });
      } else {
        parseFile(input, outputDir);
      }
    });    
  })();
})();
