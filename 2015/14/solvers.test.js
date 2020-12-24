const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const {
  normalizeInput,
  maxDistanceAfterSec,
  maxPointsAfterSec,
} = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', flow(normalizeInput, maxDistanceAfterSec(1000)), [
  {
    input: file('example.txt'),
    expectedOutput: 1120,
  },
]);

tests('Part Two', flow(normalizeInput, maxPointsAfterSec(1000)), [
  {
    input: file('example.txt'),
    expectedOutput: 689,
  },
]);
