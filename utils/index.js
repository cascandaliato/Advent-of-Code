const fs = require('fs');
const { flow, range, zip } = require('lodash');

exports.readFileLines = path => fs.readFileSync(path).toString().split('\n');

exports.splitByBlankLine = lines =>
  lines
    .join('\n')
    .split('\n\n')
    .map(g => g.split('\n'));

exports.tests = (suite, fn, tests) => {
  describe(suite, () => {
    let id = 0;
    tests.forEach(({ input, expectedOutput }) => {
      test(`#${++id}`, async () => {
        expect(await fn(input)).toBe(expectedOutput);
      });
    });
  });
};

// fn = continuation => args => {}
// and args must be JSON-serializable
exports.memoizeRecursive = (fn, baseCase) => {
  const memo = new Map();
  if (baseCase) memo.set(JSON.stringify([baseCase.in]), baseCase.out);

  const memoized = (...args) => {
    const key = JSON.stringify(args);
    if (!memo.has(key)) memo.set(key, fn(memoized)(...args));
    return memo.get(key);
  };

  return memoized;
};

exports.memoize = fn => exports.memoizeRecursive(() => fn);

exports.mod = (n, mod) => ((n % mod) + mod) % mod;

const rotate = dir => ([px, py]) => [dir * py, -dir * px];
exports.rotateCW = rotate(1);
exports.rotateCCW = rotate(-1);

exports.repeatFn = (fn, times) => flow(...range(times).fill(fn));

// https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
exports.extendedEuclidean = (a, b) => {
  let [prevR, r] = [a, b];
  let [prevS, s] = [1, 0];
  let [prevT, t] = [0, 1];
  while (r !== 0) {
    const q = Math.floor(prevR / r);
    [prevR, r] = [r, prevR - q * r];
    [prevS, s] = [s, prevS - q * s];
    [prevT, t] = [t, prevT - q * t];
  }
  return [prevS, prevT, prevR];
};

exports.gcd = (...numbers) => {
  if (numbers.length === 2) {
    return exports.extendedEuclidean(...numbers)[2];
  } else {
    return exports.gcd(numbers[0], exports.gcd(...numbers.slice(1)));
  }
};

// https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm
const modInv = (a, b) => exports.mod(exports.extendedEuclidean(a, b)[0], b);

// https://rosettacode.org/wiki/Chinese_remainder_theorem
exports.chineseRemainder = (moduli, remainders) => {
  let sum = 0;
  const product = moduli.reduce((a, b) => a * b);
  for (const [modulus, remainder] of zip(moduli, remainders)) {
    const p = product / modulus;
    sum += remainder * modInv(p, modulus) * p;
  }
  return sum % product;
};
