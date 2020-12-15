const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['0,3,6'],
    expectedOutput: 436,
  },
  {
    input: ['1,3,2'],
    expectedOutput: 1,
  },
  {
    input: ['2,1,3'],
    expectedOutput: 10,
  },
  {
    input: ['1,2,3'],
    expectedOutput: 27,
  },
  {
    input: ['2,3,1'],
    expectedOutput: 78,
  },
  {
    input: ['3,2,1'],
    expectedOutput: 438,
  },
  {
    input: ['3,1,2'],
    expectedOutput: 1836,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['0,3,6'],
    expectedOutput: 175594,
  },
  {
    input: ['1,3,2'],
    expectedOutput: 2578,
  },
  {
    input: ['2,1,3'],
    expectedOutput: 3544142,
  },
  {
    input: ['1,2,3'],
    expectedOutput: 261214,
  },
  {
    input: ['2,3,1'],
    expectedOutput: 6895259,
  },
  {
    input: ['3,2,1'],
    expectedOutput: 18,
  },
  {
    input: ['3,1,2'],
    expectedOutput: 362,
  },
]);
