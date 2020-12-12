const path = require('path');
const { upperFirst } = require('lodash');
const { readFileLines } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

const lines = readFileLines(path.join(__dirname, 'input.txt'));

const exec = (func, label) => {
  try {
    const before = Date.now();
    const answer = func(normalizeInput(lines));
    const after = Date.now();
    console.log(`Part ${upperFirst(label)}: ${answer} (${after - before}ms)`);
  } catch (e) {
    console.log(e);
  }
};

exec(solveOne, 'one');

exec(solveTwo, 'two');
