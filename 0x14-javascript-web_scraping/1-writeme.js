#!/usr/bin/node
const args = process.argv[2];
const data = process.argv[3];
const fs = require('fs');
fs.writeFile(args, data, (err) => {
  if (err) {
    console.error(err);
  }
});
