#!/usr/bin/node

let y = 0;
const value = process.argv[2];
if (value === undefined || isNaN(value)) console.log('Missing size');
while (y < value) {
  for (let i = 0; i < value; i++) {
    process.stdout.write('X');
  }
  y++;
  console.log();
}
