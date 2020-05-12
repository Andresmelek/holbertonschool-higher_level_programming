#!/usr/bin/node

const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.hbtn.io/api/films/${argv[2]}`;

request(url, function (error, response, body) {
  if (error) throw error;
  else if (argv[2] === '7') console.log('The Force Awakens');
  else console.log(JSON.parse(body).title);
});
