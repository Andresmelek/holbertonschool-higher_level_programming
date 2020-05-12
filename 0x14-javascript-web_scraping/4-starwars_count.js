#!/usr/bin/node

const argv = process.argv[2];
const request = require('request');
const list = [];

request(argv, function (error, response, body) {
  if (error) throw error;

  const results = JSON.parse(body).results;

  results.forEach(index => {
    const characters = index.characters;
    for (const actor in characters) {
      if (actor.includes('18')) list.push(actor);
    }
  });
  console.log(list.length);
});
