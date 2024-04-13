#!/usr/bin/node
const dic = require('./101-data').dict;
const vallst = Object.values(dic);
const kylst = Object.keys(dic);
const valnd = [...new Set(vallst)];
const finaldic = {};
for (let i = 0; i < valnd.length; i++) {
  const templst = [];
  for (let j = 0; j < kylst.length; j++) {
    if (dic[kylst[j]] === valnd[i]) {
      templst.push(kylst[j]);
    }
  }
  finaldic[valnd[i]] = templst;
}
console.log(finaldic);
