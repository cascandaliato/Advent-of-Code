const boxen = require('boxen');
const chalk = require('chalk');
const { upperFirst } = require('lodash');
const { readFileLines } = require('.');

module.exports = (inputPath, normalizeInput, solveOne, solveTwo) => {
  const lines = readFileLines(inputPath);

  const exec = (func, label) => {
    try {
      const before = Date.now();
      const answer = func(normalizeInput(lines));
      const after = Date.now();
      console.log(
        boxen(
          chalk`Part ${upperFirst(label)}: {green ${answer}} (${
            after - before
          }ms)`,
          { borderStyle: 'round', borderColor: 'black', padding: 1 }
        )
      );
    } catch (e) {
      console.log(e);
    }
  };

  exec(solveOne, 'one');
  exec(solveTwo, 'two');
};
