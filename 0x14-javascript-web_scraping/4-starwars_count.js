#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const films = JSON.parse(body).results;
  console.log(films.reduce((count, movie) => {
    if (movie.characters.find((character) => character.endsWith('/18/'))) {
      count += 1;
    }
    return count;
  }, 0));
});
