#!/usr/bin/node
const dict = require('./101-data').dict;
const newdic = {};
for (const i in dict) {
  newdic[dict[i]] = [];
}

for (const j in dict) {
  newdic[dict[j]].push(j);
}
console.log(newdic);
