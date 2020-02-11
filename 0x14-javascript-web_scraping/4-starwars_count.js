#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, _response, body) {
  if (err === null) {
    console.log(err);
  } else {
    let count = 0;
    JSON.parse(body).results.forEach(element => {
      element.characters.forEach(data => {
        if (data === 'https://swapi.co/api/people/18/') {
          count++;
        }
      });
    })
    ;
    console.log(count);
  }
});
