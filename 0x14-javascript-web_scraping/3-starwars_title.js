#!/usr/bin/node
const request = require('request');
request('http://swapi.co/api/films/' + process.argv[2], function (_error, _response, body) {
  console.log(JSON.parse(body).title);
});
