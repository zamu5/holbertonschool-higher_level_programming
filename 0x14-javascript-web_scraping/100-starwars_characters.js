#!/usr/bin/node
const request = require('request');
request('http://swapi.co/api/films/' + process.argv[2], function (_error, _response, body) {
  JSON.parse(body).characters.forEach(element => {
    request(element, function (_err, _res, bod) {
      console.log(JSON.parse(bod).name);
    });
  });
});
