const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example-p1.txt'),
    expectedOutput: 71,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: file('example-p2.txt'),
    expectedOutput: 132,
  },
]);
