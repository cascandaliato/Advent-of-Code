const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-one.txt'),
    expectedOutput: 4,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: file('example-one.txt'),
    expectedOutput: 32,
  },
  {
    input: file('example-two.txt'),
    expectedOutput: 126,
  },
]);
