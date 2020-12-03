const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { parse, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(parse, solveOne), [
  { input: readFileLines('03/example.txt'), expectedOutput: 7 },
]);

tests('Part Two', flow(parse, solveTwo), [
  { input: readFileLines('03/example.txt'), expectedOutput: 336 },
]);
