#!/usr/bin/node
exports.callMeMoby = function (i, func) {
  while (i > 0) {
    func.call();
    i--;
  }
};
