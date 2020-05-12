#!/usr/bin/node

const argv = process.argv;
const file = require('fs');

file.writeFile(argv[2], argv[3], 'utf-8', (error, body) => {
  if (error) {
    console.log(error);
  }
});
