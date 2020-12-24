const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['[1,2,3]'],
    expectedOutput: 6,
  },
  {
    input: ['{"a":2,"b":4}'],
    expectedOutput: 6,
  },
  {
    input: ['[[[3]]]'],
    expectedOutput: 3,
  },
  {
    input: ['{"a":{"b":4},"c":-1}'],
    expectedOutput: 3,
  },
  {
    input: ['{"a":[-1,1]}'],
    expectedOutput: 0,
  },
  {
    input: ['[-1,{"a":1}]'],
    expectedOutput: 0,
  },
  {
    input: ['[]'],
    expectedOutput: 0,
  },
  {
    input: ['{}'],
    expectedOutput: 0,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['[1,2,3]'],
    expectedOutput: 6,
  },
  {
    input: ['[1,{"c":"red","b":2},3]'],
    expectedOutput: 4,
  },
  {
    input: ['{"d":"red","e":[1,2,3,4],"f":5}'],
    expectedOutput: 0,
  },
  {
    input: ['[1,"red",5]'],
    expectedOutput: 6,
  },
]);
