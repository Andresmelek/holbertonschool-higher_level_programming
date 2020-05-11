#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let y = 0;
    while (y < this.height) {
      for (let i = 0; i < this.width; i++) {
        process.stdout.write('X');
      }
      y++;
      console.log();
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const value = this.height;
    this.width = value;
    this.height = this.width;
  }
}

module.exports = Rectangle;
