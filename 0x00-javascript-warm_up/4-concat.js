#!/usr/bin/node
let var1;
let var2;
if (process.argv.length >= 4) {
  var1 = process.argv[2];
  var2 = process.argv[3];
  console.log(var1 + ' is ' + var2);
} else if (process.argv.length === 3) {
  var1 = process.argv[2];
  console.log(var1 + ' is undefined');
} else {
  console.log('undefined is undefined');
}
