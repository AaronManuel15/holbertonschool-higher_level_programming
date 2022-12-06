#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], 'utf8', function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) throw err;
  });
});
