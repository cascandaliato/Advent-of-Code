const { tests } = require('../../utils');
const { lookAndSay } = require('./solvers');

tests('Part One', lookAndSay, [
  {
    input: '1',
    expectedOutput: '11',
  },
  {
    input: '11',
    expectedOutput: '21',
  },
  {
    input: '21',
    expectedOutput: '1211',
  },
  {
    input: '1211',
    expectedOutput: '111221',
  },
  {
    input: '111221',
    expectedOutput: '312211',
  },
]);
