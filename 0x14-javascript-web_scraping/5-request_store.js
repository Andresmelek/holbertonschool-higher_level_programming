#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];
const name = process.argv[3];
const file = require('fs');

request(argv, function (error, response, body) {
  if (error) throw error;

  file.writeFile(name, body, 'utf-8', function (error) {
    if (error) throw error;
  });
});
