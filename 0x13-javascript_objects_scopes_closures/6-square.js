#!/usr/bin/node
const Squar = require('./5-square');

class Square extends Squar {
  charPrint (c) {
    let ret = ''; let i; let j; let data;
    c ? data = c : data = 'X';
    for (j = 0; j < this.width; j++) {
      ret += data;
    }
    for (i = 0; i < this.height; i++) {
      console.log(ret);
    }
  }
}
module.exports = Square;
