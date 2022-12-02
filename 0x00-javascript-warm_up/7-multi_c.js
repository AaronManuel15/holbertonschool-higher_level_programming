#!/usr/bin/node
const occ = parseInt(process.argv[2]);
if (occ) {
  for (let i = 0; i < occ; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
