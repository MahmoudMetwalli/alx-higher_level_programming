#!/usr/bin/node
/* yeah! */

const array = process.argv;
const converted = [];
let i = 2;
while (array[i] !== undefined) {
  converted.push(parseInt(array[i]));
  i += 1;
}
if (converted.length === 0 || converted.length === 1) {
  console.log('0');
} else {
  i = 1;
  let target = converted[0];
  let subtarget = converted[0];
  while (i < converted.length) {
    if (target < converted[i]) {
      target = converted[i];
    }
    i += 1;
  }
  i = 1;
  while (i < converted.length) {
    if (target === converted[i]) {
      subtarget = subtarget;
    } else if (subtarget < converted[i]) {
      subtarget = converted[i];
    }
    i += 1;
  }
  console.log(subtarget);
}
