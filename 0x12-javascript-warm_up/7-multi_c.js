#!/usr/bin/node
if (process.argv.length === 2 || isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
