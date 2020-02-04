#!/usr/bin/node
if (process.argv.length === 2 || isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  let i; let j; let ret;
  for (i = 0; i < Number(process.argv[2]); i++) {
    ret = '';
    for (j = 0; j < Number(process.argv[2]); j++) {
      ret = ret + 'X';
    }
    console.log(ret);
  }
}
