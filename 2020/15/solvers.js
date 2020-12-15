exports.normalizeInput = lines => lines[0].split(',').map(Number);

const speakNth = n => startingNumbers => {
  const lastSpokenAt = new Uint32Array(n);
  startingNumbers.slice(0, -1).map((num, idx) => (lastSpokenAt[num] = idx + 1));
  let last = startingNumbers.slice(-1)[0];

  for (let round = startingNumbers.length + 1; round <= n; round++) {
    const speak = lastSpokenAt[last] !== 0 ? round - 1 - lastSpokenAt[last] : 0;
    lastSpokenAt[last] = round - 1;
    last = speak;
  }

  return last;
};

exports.solveOne = speakNth(2020);

exports.solveTwo = speakNth(30000000);
