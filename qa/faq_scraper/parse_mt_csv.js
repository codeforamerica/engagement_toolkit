(function(){
  var fs = require('fs'),
      inputFile = process.argv[2],
      headers,
      lines,
      i;

  var parseLine = function(line) {
    //NOTE: this leave extra double-quotes on the first and last value
    var values = line.split('","'),
        val, 
        c, 
        data = {
          properties: {},
          questions: [],
          answers: []
        };
    
    for (c=0; c<headers.length; c++) {
      val = strip(values[c]);
      
      if (val) {
        if (headers[c].lastIndexOf('A') === headers[c].length-1) {
          data.answers[headers[c].split('.')[1].replace('A', '')] = val;
        } else if (headers[c].lastIndexOf('Q') === headers[c].length-1) {
          data.questions[headers[c].split('.')[1].replace('Q', '')] = val;
        } else {
          data.properties[headers[c]] = val;        
        }
      }
    }
    
    return data;
  };
  
  var logCsv = function(data) {
    var qNum, line,
        url = data.properties['Input.url'],
        date = data.properties['CreationTime'];
    
    for(qNum in data.questions) {
      line = '"' + url + '","' + date + '","' + 
          qNum + '","' + data.questions[qNum]  + '","' + data.answers[qNum] + '"'; 

      console.log(line);
    }
  };
  
  var strip = function(str) {
    return str ? str.replace(/"\r*/, '').trim() : null;
  };
  
  //fileStr = fs.readFileSync('Batch_505552_batch_results (1).csv').toString();
  
  fileStr = fs.readFileSync(inputFile).toString();
  fileStr = fileStr.replace(/([^"])(\r\n)+/g, '$1 ');
  //console.log(fileStr);
  
  lines = fileStr.split('\n');
  //NOTE: this leave extra double-quotes on the first and last value
  headers = lines[0].split('","');
  headers[0] = strip(headers[0]);
  headers[headers.length-1] = strip(headers[headers.length-1]);
  
  
  console.log('"url","createDate","questionNumber","question","answer"');
  for (i=1; i<lines.length; i++) {
    logCsv(parseLine(lines[i]));
  }
  
})();
