#!/usr/bin/node
let response;
if (process.argv.length === 2) {
  response = 'No argument';
} else if (process.argv.length === 3) {
  response = 'Argument found';
} else {
  response = 'Arguments found';
}

console.log(response);
