#!/usr/bin/node

const list = [];

if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    list.push(parseInt(process.argv[i], 10));
  }
  list.sort();
  const max = Math.max(...list);
  const index = list.indexOf(max);
  list.splice(index, 1);
  console.log(Math.max(...list));
}
