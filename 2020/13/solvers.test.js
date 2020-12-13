const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: file('example.txt'),
    expectedOutput: 295,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: file('example-p2-1.txt'),
    expectedOutput: 1068781,
  },
  {
    input: file('example-p2-2.txt'),
    expectedOutput: 3417,
  },
  {
    input: file('example-p2-3.txt'),
    expectedOutput: 754018,
  },
  {
    input: file('example-p2-4.txt'),
    expectedOutput: 779210,
  },
  {
    input: file('example-p2-5.txt'),
    expectedOutput: 1261476,
  },
  {
    input: file('example-p2-6.txt'),
    expectedOutput: 1202161486,
  },
]);
