#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  rotate () {
    const store = this.width;
    this.width = this.height;
    this.height = store;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
