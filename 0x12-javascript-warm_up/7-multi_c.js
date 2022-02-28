#!/usr/bin/node
const love = 'C is fun';
const num = process.argv[5];
let i = 0;
if (parseInt(num)) {
  while (i < num) {
    console.log(love);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
