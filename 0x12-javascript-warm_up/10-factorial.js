#!/usr/bin/node

if (process.argv[2] === undefined) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2], 10)));
}

function factorial (value) {
  let result = 1;
  for (let i = 1; i <= value; i++) {
    result *= i;
  }
  return result;
}
