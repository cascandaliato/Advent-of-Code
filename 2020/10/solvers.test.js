const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-p1-1.txt'),
    expectedOutput: 7 * 5,
  },
  {
    input: file('example-p1-2.txt'),
    expectedOutput: 22 * 10,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: file('example-p1-1.txt'),
    expectedOutput: 8,
  },
  {
    input: file('example-p1-2.txt'),
    expectedOutput: 19208,
  },
]);
