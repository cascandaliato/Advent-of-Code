const path = require('path');
const { flow } = require('lodash');
const { readFileLines, tests } = require('../../utils');
const {
  normalizeInput,
  getCombos,
  getCombosMinContainers,
} = require('./solvers');

const file = fileName => readFileLines(path.join(__dirname, fileName));

tests('Part One', input => getCombos(25, normalizeInput(input)).length, [
  {
    input: file('example.txt'),
    expectedOutput: 4,
  },
]);

tests(
  'Part Two',
  input => getCombosMinContainers(25, normalizeInput(input)).length,
  [
    {
      input: file('example.txt'),
      expectedOutput: 3,
    },
  ]
);
