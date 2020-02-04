#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const ar = [];
  let i;
  for (i = 2; process.argv[i]; i++) {
    ar.push(parseInt(process.argv[i]));
  }
  console.log(ar.sort().reverse()[1]);
}
