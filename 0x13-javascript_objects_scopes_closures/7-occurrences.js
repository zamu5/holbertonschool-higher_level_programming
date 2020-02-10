#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  list.forEach(element => {
    if (element === searchElement) {
      cont++;
    }
  });
  return cont;
}
;
