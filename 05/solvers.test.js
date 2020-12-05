const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { solveOne, solveTwo, parse } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(parse, solveOne), [
  {
    input: ['FBFBBFFRLR'],
    expectedOutput: 357,
  },
  {
    input: ['BFFFBBFRRR'],
    expectedOutput: 567,
  },
  {
    input: ['FFFBBBFRRR'],
    expectedOutput: 119,
  },
  {
    input: ['BBFFBBFRLL'],
    expectedOutput: 820,
  },
]);
