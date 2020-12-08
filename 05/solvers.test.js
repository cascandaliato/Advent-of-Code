const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { normalizeInput, solveOne } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-p1-1.txt'),
    expectedOutput: 357,
  },
  {
    input: file('example-p1-2.txt'),
    expectedOutput: 567,
  },
  {
    input: file('example-p1-3.txt'),
    expectedOutput: 119,
  },
  {
    input: file('example-p1-4.txt'),
    expectedOutput: 820,
  },
]);
