#!/usr/bin/node

const argv = process.argv[2];
const request = require('request');
let count = 0;

request(argv, function (error, response, body) {
  if (error) throw error;

  const results = JSON.parse(body).results;

  results.forEach(index => {
    const characters = index.characters;
    for (const actor in characters) {
      if (characters[actor].includes('18')) {
        count++;
      }
    }
  });
  console.log(count);
});
