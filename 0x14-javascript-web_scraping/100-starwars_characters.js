#!/usr/bin/node
const args = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + args;
const request = require('request');
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
