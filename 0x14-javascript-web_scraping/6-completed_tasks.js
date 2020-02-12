#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (_error, _response, body) {
  const newDir = {};
  JSON.parse(body).forEach(element => {
    if (element.completed === true) {
      if (newDir[element.userId]) {
        newDir[element.userId] += 1;
      } else {
        newDir[element.userId] = 1;
      }
    }
  });
  console.log(newDir);
});
