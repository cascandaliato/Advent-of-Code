const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['50'],
    expectedOutput: 4,
  },
]);
