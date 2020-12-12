const crypto = require('crypto');

exports.normalizeInput = lines => lines[0];

const solve = numZeros => async key => {
  const target = Array(numZeros).fill(0).join('');

  let i = 1;
  while (
    crypto
      .createHash('md5')
      .update(`${key}${i}`)
      .digest('hex')
      .slice(0, numZeros) !== target
  )
    i += 1;

  return i;
};

exports.solveOne = solve(5);

exports.solveTwo = solve(6);
