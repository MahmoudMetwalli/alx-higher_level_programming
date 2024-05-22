#!/usr/bin/node
const args = process.argv[2];
const request = require('request');
request(args, (err, response) => {
  if (err) {
  console.error(err);
  return;}
  console.log('Code:', response.statusCode); // Print the response status code if a response was received
});
