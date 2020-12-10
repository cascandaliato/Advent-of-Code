const { countBy } = require('lodash');

exports.normalizeInput = lines => {
  const numbers = lines.map(Number).sort((a, b) => a - b);
  return [0, ...numbers, numbers[numbers.length - 1] + 3];
};

exports.solveOne = outputs => {
  const { 1: ones, 3: threes } = countBy(
    outputs.slice(1).map((output, idx) => output - outputs[idx])
  );
  return ones * threes;
};

exports.solveTwo = outputs => {
  const memo = {};

  const dp = start => {
    if (start in memo) return memo[start];
    if (start === outputs.length - 1) return 1;

    let combos = 0;
    for (
      let i = start + 1;
      i < outputs.length && outputs[i] - outputs[start] <= 3;
      i++
    ) {
      combos += dp(i);
    }

    memo[start] = combos;
    return combos;
  };

  return dp(0);
};
