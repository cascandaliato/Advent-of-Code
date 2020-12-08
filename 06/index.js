const path = require('path');
const { readFileLines } = require('../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const lines = readFileLines(path.join(__dirname, 'input.txt'));

console.log('Part One:', solveOne(normalizeInput(lines)));

console.log('Part Two:', solveTwo(normalizeInput(lines)));
