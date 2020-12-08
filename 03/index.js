const path = require('path');
const { readFileLines } = require('../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const lines = readFileLines(path.join(__dirname, 'input.txt'));

try {
  console.log('Part One:', solveOne(normalizeInput(lines)));
} catch (e) {
  console.log(e);
}

try {
  console.log('Part Two:', solveTwo(normalizeInput(lines)));
} catch (e) {
  console.log(e);
}
