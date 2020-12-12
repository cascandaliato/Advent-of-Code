const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['2x3x4'],
    expectedOutput: 58,
  },
  {
    input: ['1x1x10'],
    expectedOutput: 43,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['2x3x4'],
    expectedOutput: 34,
  },
  {
    input: ['1x1x10'],
    expectedOutput: 14,
  },
]);
