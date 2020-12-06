const path = require('path');
const { readFileLines } = require('../utils');
const { parse, solveOne, solveTwo } = require('./solvers');

const lines = readFileLines(path.join(__dirname, 'input.txt'));

console.log('Part One:', solveOne(parse(lines)));

console.log('Part Two:', solveTwo(parse(lines)));
