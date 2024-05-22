#!/usr/bin/node
const args = process.argv[2];
const fs = require('fs');
fs.readFile(args, (err, data) => {
	if (err) {
	  console.error(err);
	  return;
	}
	console.log(data.toString());
  });
