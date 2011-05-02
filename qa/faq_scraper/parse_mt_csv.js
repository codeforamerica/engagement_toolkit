(function(){
  var fs = require('fs');

  var parseLine = function(line, headers) {
    //NOTE: this leave extra double-quotes on the first and last value
    var values = line.split('","'),
        url, date, 
        parsedLines = [],
        data = {
          properties: {},
          questions: [],
          answers: []
        };
    
    headers.forEach(function(header, c) {
      val = strip(values[c]);
      
      if (val) {
        if (header.lastIndexOf('A') === header.length-1) {
          //If this is an answer, parse out the answer number from the key and 
          //save the value
          data.answers[parseInt(header.split('.')[1].replace('A', ''), 10)] = val;
        } else if (header.lastIndexOf('Q') === header.length-1) {
          //If this is an question, parse out the question number from the key 
          //and save the value
          data.questions[parseInt(header.split('.')[1].replace('Q', ''), 10)] = val;
        } else {
          //These are other properties of the question
          data.properties[header] = val;        
        }
      }
    });
    
    url = data.properties['Input.url'];
    date = data.properties['CreationTime'];
    data.questions.forEach(function(question, qNum) {
      parsedLines.push({
        "url": url,
        "createDate": date,
        "questionNumber": qNum,
        "question": question,
        "answer": data.answers[qNum]
      });
    });
    
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
    return str ? str.replace(/"\r*/, '').trim() : null;
  };
  
  //Init
  (function() {
    var inputFile = process.argv[2],
        fileStr,
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
            
      //console.log(dedupedData);
      console.log(toCsv(dedupe(parsedData)));

    } else {
      console.log('Usage: node parse_mt_csv.js turk_file_to_parse.csv');
    }
  })();
})();
