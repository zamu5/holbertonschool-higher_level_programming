#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2], function (_error, _response, body) {
  fs.writeFile(process.argv[3], body, (err, data) => {
    if (err) {
      console.log(err);
    }
  })
  ;
});
