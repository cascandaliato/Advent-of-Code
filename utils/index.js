const fs = require('fs');
const { flow, range } = require('lodash');

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
