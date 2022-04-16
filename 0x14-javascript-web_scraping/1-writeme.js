#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], process.argv[3], 'utf8', (err, data) => {
  if (err) {
    console.err(err);
    return;
  }
  console.log(data);
});
