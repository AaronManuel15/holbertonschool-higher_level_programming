#!/usr/bin/node
function factorial (number) {
  if (number > 0) {
    return number * factorial(number - 1);
  } else {
    return 1;
  }
}

const number = +process.argv[2];
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
