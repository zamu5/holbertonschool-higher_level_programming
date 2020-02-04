#!/usr/bin/node
if (process.argv.length === 2 || isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(Number(process.argv[2])));
}
