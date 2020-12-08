const fs = require('fs');

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
      test(`#${++id}`, () => {
        expect(fn(input)).toBe(expectedOutput);
      });
    });
  });
};
