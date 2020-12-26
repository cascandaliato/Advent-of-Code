const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const {
  normalizeInput,
  gameOfLife,
  gameOfLifeWithPillars,
} = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, gameOfLife(5)), [
  {
    input: file('example.txt'),
    expectedOutput: 4,
  },
]);

tests('Part Two', flow(normalizeInput, gameOfLifeWithPillars(5)), [
  {
    input: file('example.txt'),
    expectedOutput: 17,
  },
]);
