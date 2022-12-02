#!/usr/bin/node
let response;
if (process.argv.length <= 2) {
  console.log('No argument');
} else {
  response = process.argv.slice(2);
  console.log(response[0]);
}
