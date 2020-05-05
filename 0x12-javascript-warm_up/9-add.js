#!/usr/bin/node

if (process.argv <= 3) {
  console.log(isNaN);
} else {
  console.log(add(parseInt(process.argv[2], 10), parseInt(process.argv[3]), 10));
}
function add (a, b) {
  return a + b;
}
