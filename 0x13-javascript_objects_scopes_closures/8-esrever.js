#!/usr/bin/node
exports.esrever = function (list) {
  const listReturn = []; let va;
  while (list[0]) {
    va = list.pop();
    listReturn.push(va);
  }
  return listReturn;
};
