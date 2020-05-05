#!/usr/bin/node

const convert = parseInt(process.argv[2], 10);
if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convert}`);
}
