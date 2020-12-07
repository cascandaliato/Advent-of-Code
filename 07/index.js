const path = require('path');
const { readFileLines } = require('../utils');
const { parse, solveOne, solveTwo } = require('./solvers');

const lines = readFileLines(path.join(__dirname, 'input.txt'));

try {
  console.log('Part One:', solveOne(parse(lines)));
} catch (e) {
  console.log(e);
}

try {
  console.log('Part Two:', solveTwo(parse(lines)));
} catch (e) {
  console.log(e);
}
