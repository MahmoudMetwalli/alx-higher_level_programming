#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/people/18/';
const request = require('request');
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).films.length);
});
