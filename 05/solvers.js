const { flow, range } = require('lodash');

exports.parse = lines =>
  new Set(
    lines.map(
      flow(replaceZeroOnes('F', 'B'), replaceZeroOnes('L', 'R'), b =>
        parseInt(b, 2)
      )
    )
  );

const replaceZeroOnes = (zero, one) => s =>
  s.replace(new RegExp(zero, 'g'), '0').replace(new RegExp(one, 'g'), '1');

exports.solveOne = ids => [...ids].reduce((a, b) => Math.max(a, b), 0);

exports.solveTwo = ids =>
  range(2 ** 10)
    // remove front and back rows
    .filter(id => id >= 8 && id < 2 ** 10 - 8)
    // keep only empty seats/ids that are next to occupied seats
    .filter(id => !ids.has(id) && ids.has(id - 1) && ids.has(id + 1))[0];
