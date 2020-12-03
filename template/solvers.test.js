const { flow } = require('lodash');
const { readFileLines, tests } = require('../utils');
const { solveOne, solveTwo, parse } = require('./solvers');

tests('Part One', flow(parse, solveOne), [
  { input: readFileLines('03/example.txt'), expectedOutput: undefined },
]);

tests('Part Two', flow(parse, solveTwo), [
  { input: readFileLines('03/example.txt'), expectedOutput: undefined },
]);
