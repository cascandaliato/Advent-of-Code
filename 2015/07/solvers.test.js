const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-1.txt'),
    expectedOutput: 123,
  },
  {
    input: file('example-2.txt'),
    expectedOutput: 456,
  },
  {
    input: file('example-3.txt'),
    expectedOutput: 72,
  },
  {
    input: file('example-4.txt'),
    expectedOutput: 507,
  },
  {
    input: file('example-5.txt'),
    expectedOutput: 492,
  },
  {
    input: file('example-6.txt'),
    expectedOutput: 114,
  },
  {
    input: file('example-7.txt'),
    expectedOutput: 65412,
  },
  {
    input: file('example-8.txt'),
    expectedOutput: 65079,
  },
]);
