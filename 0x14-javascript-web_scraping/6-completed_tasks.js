#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const dic = {};

request(url, function (error, responde, body) {
  if (error) console.log(error);

  const tasks = JSON.parse(body);

  tasks.forEach(task => {
    if (task.completed) {
      if (dic[task.userId] === undefined) {
        dic[task.userId] = 1;
      } else {
        dic[task.userId] += 1;
      }
    }
  });
  console.log(dic);
});
