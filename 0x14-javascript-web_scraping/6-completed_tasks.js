#!/usr/bin/node
const request = require('request');
const args = process.argv[2];
const url = args + '?completed=true';
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const list = {};
  todos.forEach((todo) => {
    if (list[todo.userId]) {
      list[todo.userId] += 1;
    } else {
      list[todo.userId] = 1;
    }
  });
  console.log(list);
});
