#!/usr/bin/node
const request = require('request');
const util = require('util');
const args = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + args;

// Convert the request function to a Promise-based one
const requestPromise = util.promisify(request);

async function getCharacterNames () {
  try {
    const response = await requestPromise(url);
    const characters = JSON.parse(response.body).characters;
    for (const character of characters) {
      const characterResponse = await requestPromise(character);
      console.log(JSON.parse(characterResponse.body).name);
    }
  } catch (err) {
    console.error(err);
  }
}

getCharacterNames();
