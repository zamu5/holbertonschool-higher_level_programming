#!/usr/bin/node
let fac = 1; let i;
for (i = 1; i <= parseInt(process.argv[2]); i++) {
  fac = fac * i;
}
console.log(fac);
