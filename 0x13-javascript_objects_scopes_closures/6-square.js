#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.standout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
}

module.exports = Square;
