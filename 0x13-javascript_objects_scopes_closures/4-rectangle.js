#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let ret = ''; let i; let j;
    for (j = 0; j < this.width; j++) {
      ret += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(ret);
    }
  }

  rotate () {
    this.height += this.width;
    this.width = this.height - this.width;
    this.height -= this.width;
  }

  double () {
    this.width += this.width;
    this.height += this.height;
  }
}
module.exports = Rectangle;
