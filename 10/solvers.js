const { countBy } = require('lodash');

exports.normalizeInput = lines => {
  const numbers = lines.map(Number).sort((a, b) => a - b);
  return [...numbers, numbers.slice(-1)[0] + 3];
};

exports.solveOne = outputs => {
  const { 1: ones, 3: threes } = countBy(
    outputs.map((output, idx) => output - (outputs[idx - 1] || 0))
  );
  return ones * threes;
};

exports.solveTwo = outputs => {
  const combos = new Map([[0, 1]]);

  outputs.forEach(output =>
    combos.set(
      output,
      (combos.get(output - 1) || 0) +
        (combos.get(output - 2) || 0) +
        (combos.get(output - 3) || 0)
    )
  );

  return combos.get(outputs.slice(-1)[0]);
};
