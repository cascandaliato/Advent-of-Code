const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { solveOne, solveTwo, parse } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(parse, solveOne), [
  {
    input: file('example.txt'),
    expectedOutput: 11,
  },
]);

tests('Part Two', flow(parse, solveTwo), [
  {
    input: file('example.txt'),
    expectedOutput: 6,
  },
]);
