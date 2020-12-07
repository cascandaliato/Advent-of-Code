const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { solveOne, solveTwo, parse } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(parse, solveOne), [
  {
    input: file('example-one.txt'),
    expectedOutput: 4,
  },
]);

tests('Part Two', flow(parse, solveTwo), [
  {
    input: file('example-one.txt'),
    expectedOutput: 32,
  },
  {
    input: file('example-two.txt'),
    expectedOutput: 126,
  },
]);
