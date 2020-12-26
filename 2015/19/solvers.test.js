const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-p1-1.txt'),
    expectedOutput: 4,
  },
  {
    input: file('example-p1-2.txt'),
    expectedOutput: 7,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: file('example-p2-1.txt'),
    expectedOutput: 3,
  },
  {
    input: file('example-p2-2.txt'),
    expectedOutput: 6,
  },
]);
