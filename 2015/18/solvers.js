const { flow } = require('lodash');
const { toMatrix } = require('../../utils');
const ca = require('../../utils/cell-automata');

const alive = '#';
const dead = '.';

exports.normalizeInput = toMatrix;

exports.gameOfLife = generations =>
  flow(
    ca.conwayFinite({ alive, dead }),
    ca.evolve(generations),
    ca.countByState(alive)
  );

exports.solveOne = exports.gameOfLife(100);

const isCorner = ([r, c], matrix) =>
  (r === 0 || r === matrix.length - 1) &&
  (c === 0 || c === matrix[0].length - 1);

exports.gameOfLifeWithPillars = generations => matrix => {
  matrix[0][0] = alive;
  matrix[0][matrix[0].length - 1] = alive;
  matrix[matrix.length - 1][0] = alive;
  matrix[matrix.length - 1][matrix[0].length - 1] = alive;

  return flow(
    ca.conwayFinite({
      alive,
      dead,
      overrides: {
        cell: {
          defaultState: dead,
          states: {
            [alive]: (coords, nEntries) =>
              isCorner(coords, matrix)
                ? alive
                : [2, 3].includes(ca.countEntriesByState(nEntries, alive))
                ? alive
                : dead,
            [dead]: (coords, nEntries) =>
              isCorner(coords, matrix)
                ? alive
                : ca.countEntriesByState(nEntries, alive) === 3
                ? alive
                : dead,
          },
        },
      },
    }),
    ca.evolve(generations),
    ca.countByState(alive)
  )(matrix);
};

exports.solveTwo = exports.gameOfLifeWithPillars(100);
