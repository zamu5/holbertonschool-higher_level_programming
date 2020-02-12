#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, _response, body) {
  if (err === null) {
    let count = 0;
    JSON.parse(body).results.forEach(element => {
      element.characters.forEach(data => {
        if (data.search('/18/') > 0) {
          count++;
        }
      });
    })
    ;
    console.log(count);
  }
});
