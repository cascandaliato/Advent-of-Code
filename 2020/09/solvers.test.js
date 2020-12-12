const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

const PREAMBLE = 5;

tests('Part One', input => solveOne(normalizeInput(input), PREAMBLE), [
  {
    input: file('example.txt'),
    expectedOutput: 127,
  },
]);

tests('Part Two', input => solveTwo(normalizeInput(input), PREAMBLE), [
  {
    input: file('example.txt'),
    expectedOutput: 62,
  },
]);
