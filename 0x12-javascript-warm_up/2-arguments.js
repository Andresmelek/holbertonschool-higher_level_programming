#!/usr/bin/node

var len = process.argv.length;

if (len === 3) {
  console.log('Argument found');
} else if (len > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
