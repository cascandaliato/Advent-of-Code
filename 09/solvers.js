const PREAMBLE = 25;

exports.normalizeInput = lines => lines.map(Number);

// assuming no repeats
exports.solveOne = (numbers, preamble = PREAMBLE) => {
  const recentlySeen = new Set(numbers.slice(0, preamble));
  for (let i = preamble; i < numbers.length; i++) {
    if (![...recentlySeen].some(v => recentlySeen.has(numbers[i] - v))) {
      return numbers[i];
    }

    recentlySeen.add(numbers[i]);
    recentlySeen.delete(numbers[i - preamble]);
  }
};

exports.solveTwo = (numbers, preamble = PREAMBLE) => {
  const target = exports.solveOne(numbers, preamble);

  let lo = 0;
  let hi = 2;
  let sum = numbers[0] + numbers[1];

  while (sum !== target) {
    if (sum > target) {
      sum -= numbers[lo];
      lo++;
    }
    if (sum < target || hi - lo === 1) {
      sum += numbers[hi];
      hi++;
    }
  }
  return (
    numbers.slice(lo, hi).reduce((a, b) => Math.min(a, b)) +
    numbers.slice(lo, hi).reduce((a, b) => Math.max(a, b))
  );
};
