exports.normalizeInput = lines => new Set(lines.map(Number));

const findTwo = targetSum => numbers => {
  for (const n of numbers) {
    if (numbers.has(targetSum - n)) {
      return n * (targetSum - n);
    }
  }
};

exports.solveOne = findTwo(2020);

const findThree = targetSum => numbers => {
  for (const n of numbers) {
    const two = findTwo(targetSum - n)(numbers);
    if (two) return n * two;
  }
};

exports.solveTwo = findThree(2020);
