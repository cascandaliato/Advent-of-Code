exports.normalizeInput = lines => lines[0].split(',').map(Number);

const speakNth = n => startingNumbers => {
  const numbersSpoken = new Map(
    startingNumbers.slice(0, -1).map((num, idx) => [num, idx + 1])
  );
  let last = startingNumbers.slice(-1)[0];

  for (let round = startingNumbers.length + 1; round <= n; round++) {
    const speak = round - 1 - numbersSpoken.get(last) || 0;
    numbersSpoken.set(last, round - 1);
    last = speak;
  }
  return last;
};

exports.solveOne = speakNth(2020);

exports.solveTwo = speakNth(30000000);
