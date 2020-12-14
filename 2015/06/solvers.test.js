const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['turn on 0,0 through 999,999'],
    expectedOutput: 1000000,
  },
  {
    input: ['toggle 0,0 through 999,0'],
    expectedOutput: 1000,
  },
  {
    input: [
      'turn on 0,0 through 999,999',
      'toggle 0,0 through 999,0',
      'turn off 499,499 through 500,500',
    ],
    expectedOutput: 1000000 - 1000 - 4,
  },
  {
    input: ['turn off 499,499 through 500,500'],
    expectedOutput: 0,
  },
]);
