const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { solveOne, solveTwo, parse } = require('./solvers');

tests('Part One', flow(parse, solveOne), [
  {
    input: readFileLines(path.join(__dirname, 'example-one.txt')),
    expectedOutput: 2,
  },
]);

tests('Part Two', flow(parse, solveTwo), [
  {
    input: readFileLines(path.join(__dirname, 'example-two-invalid.txt')),
    expectedOutput: 0,
  },
  {
    input: readFileLines(path.join(__dirname, 'example-two-valid.txt')),
    expectedOutput: 4,
  },
]);
