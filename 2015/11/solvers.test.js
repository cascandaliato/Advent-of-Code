const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['abcdefgh'],
    expectedOutput: 'abcdffaa',
  },
  {
    input: ['ghijklmn'],
    expectedOutput: 'ghjaabcc',
  },
]);
