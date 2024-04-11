#!/usr/bin/node
/* function that executes x times a function */

function addMeMaybe (a, func) {
  a++;
  func(a);
}
module.exports = { addMeMaybe };
