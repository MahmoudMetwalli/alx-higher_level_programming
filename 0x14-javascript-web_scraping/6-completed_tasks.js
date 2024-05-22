#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todos = JSON.parse(body);
  const list = {};
  todos.forEach((todo) => {
    if (todo.completed && list[todo.userId] === undefined) {
      list[todo.userId] = 1;
    } else if (todo.completed) {
      list[todo.userId] += 1;
    }
  });
  console.log(list);
});
