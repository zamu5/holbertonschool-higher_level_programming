#!/usr/bin/node
const list1 = require('./100-main').list;
const newlist = list1.map(function (value, index) {
  return value * index;
});
console.log(list1);
console.log(newlist);
