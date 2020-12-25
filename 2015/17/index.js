const path = require('path');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

(async () => {
  await require('../../utils/runner')(
    path.join(__dirname, 'input.txt'),
    normalizeInput,
    solveOne,
    solveTwo
  );
})();
