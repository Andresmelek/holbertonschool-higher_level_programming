#!/usr/bin/node

const argv = process.argv;
const file = require('fs');

file.readFile(argv[2], 'utf-8', (error, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(body);
  }
});
