#!/usr/bin/node

const value = process.argv[2];
if (value === undefined) console.log('Missing number of occurrences');
for (let i = 0; i < value; i++) {
  console.log('C is fun');
}
