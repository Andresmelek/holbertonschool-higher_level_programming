#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
const newlist = list.map((index, value) => value * index);
console.log(newlist);
