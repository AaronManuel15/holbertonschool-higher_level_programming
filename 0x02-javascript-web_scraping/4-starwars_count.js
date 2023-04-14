#!/usr/bin/node

const request = require('request');
let movieCount = 0;

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  const data = JSON.parse(body).results;
  for (const movie in data) {
    const chars = data[movie].characters;
    for (const char in chars) {
      if (chars[char].includes('/18/')) {
        movieCount++;
      }
    }
  }
  console.log(movieCount);
});
