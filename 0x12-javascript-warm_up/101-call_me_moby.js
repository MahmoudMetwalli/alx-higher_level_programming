#!/usr/bin/node
/* function that executes x times a function */

function callMeMoby (a, func) {
  for (let i = 0; i < a; i++) {
    func();
  }
}
module.exports = { callMeMoby };
