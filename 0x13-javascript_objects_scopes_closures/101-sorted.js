#!/usr/bin/node
const dict1 = require('./101-data.js').dict;
const newDict = {};
for (const _k in dict1) {
  if (dict1[_k] in newDict) {
    newDict[dict1[_k]].push(_k);
  } else {
    newDict[dict1[_k]] = [];
    newDict[dict1[_k]].push(_k);
  }
}
console.log(newDict);
