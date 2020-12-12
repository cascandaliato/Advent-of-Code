const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['abcdef'],
    expectedOutput: 609043,
  },
  {
    input: ['pqrstuv'],
    expectedOutput: 1048970,
  },
]);
