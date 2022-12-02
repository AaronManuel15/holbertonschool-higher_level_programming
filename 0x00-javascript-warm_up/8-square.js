#!/usr/bin/node
const occ = parseInt(process.argv[2]);
if (occ) {
  let row = '';
  for (let i = 0; i < occ; i++) {
    row += 'X';
  }
  for (let i = 0; i < occ; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
