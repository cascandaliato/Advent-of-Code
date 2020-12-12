const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['(())'],
    expectedOutput: 0,
  },
  {
    input: ['()()'],
    expectedOutput: 0,
  },
  {
    input: ['((('],
    expectedOutput: 3,
  },
  {
    input: ['(()(()('],
    expectedOutput: 3,
  },
  {
    input: ['))((((('],
    expectedOutput: 3,
  },
  {
    input: ['())'],
    expectedOutput: -1,
  },
  {
    input: ['))('],
    expectedOutput: -1,
  },
  {
    input: [')))'],
    expectedOutput: -3,
  },
  {
    input: [')())())'],
    expectedOutput: -3,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: [')'],
    expectedOutput: 1,
  },
  {
    input: ['()())'],
    expectedOutput: 5,
  },
]);
