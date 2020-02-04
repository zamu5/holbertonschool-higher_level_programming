#!/usr/bin/node
const fac = fact(parseInt(process.argv[2]));
function fact (number) {
  let i; let res = 1;
  for (i = 1; i <= number; i++) {
    res = res * i;
  }
  return res;
}
console.log(fac);
