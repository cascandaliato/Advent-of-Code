const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['1 + 2 * 3 + 4 * 5 + 6'],
    expectedOutput: 71,
  },
  {
    input: ['1 + (2 * 3) + (4 * (5 + 6))'],
    expectedOutput: 51,
  },
  {
    input: ['2 * 3 + (4 * 5)'],
    expectedOutput: 26,
  },
  {
    input: ['5 + (8 * 3 + 9 + 3 * 4 * 3)'],
    expectedOutput: 437,
  },
  {
    input: ['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'],
    expectedOutput: 12240,
  },
  {
    input: ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'],
    expectedOutput: 13632,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['1 + 2 * 3 + 4 * 5 + 6'],
    expectedOutput: 231,
  },
  {
    input: ['1 + (2 * 3) + (4 * (5 + 6))'],
    expectedOutput: 51,
  },
  {
    input: ['2 * 3 + (4 * 5)'],
    expectedOutput: 46,
  },
  {
    input: ['5 + (8 * 3 + 9 + 3 * 4 * 3)'],
    expectedOutput: 1445,
  },
  {
    input: ['5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'],
    expectedOutput: 669060,
  },
  {
    input: ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'],
    expectedOutput: 23340,
  },
]);
