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
}

module.exports = Rectangle;
