#!/usr/bin/node
let str;
if (process.argv.length < 1)
	str = 'No argument';
else if (process.argv.length === 1)
	str = 'Argument found';
else
	str = 'Arguments found';
console.log(str);
