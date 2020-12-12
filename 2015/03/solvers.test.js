const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['>'],
    expectedOutput: 2,
  },
  {
    input: ['^>v<'],
    expectedOutput: 4,
  },
  {
    input: ['^v^v^v^v^v'],
    expectedOutput: 2,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['^v'],
    expectedOutput: 3,
  },
  {
    input: ['^>v<'],
    expectedOutput: 3,
  },
  {
    input: ['^v^v^v^v^v'],
    expectedOutput: 11,
  },
]);
