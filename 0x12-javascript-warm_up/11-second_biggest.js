#!/usr/bin/node
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const ar = []; let i;
  for (i = 2; process.argv[i]; i++) {
    ar.push(parseInt(process.argv[i]));
  }
  i = 0;
  ar.sort().reverse();
  while (ar[i] === ar[i + 1]) {
    i++;
  }
  console.log(ar[i + 1]);
}
