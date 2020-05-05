#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2], 10)));
}

function factorial (value) {
  if (value === 0) return 1;
  else return value * factorial(value - 1);
}
