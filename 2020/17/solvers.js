const { combos } = require('../../utils');
const Grid = require('../../utils/sparse-hyper-matrix');

const status = { '#': 1, '.': 0 };

exports.normalizeInput = lines =>
  lines.map(line => [...line].map(ch => status[ch]));

const directions = dimensions =>
  combos([0, -1, 1], dimensions).filter(combo => !combo.every(v => v === 0));

const withNeighbors = (grid, deltas) =>
  [
    ...new Set([
      ...[...grid].map(coords => coords.slice(0, -1).join(',')),
      ...[...grid]
        .flatMap(coords =>
          deltas.map(delta => delta.map((d, idx) => d + coords[idx]))
        )
        .map(arr => arr.join(',')),
    ]),
  ].map(str => str.split(',').map(Number));

const solve = dimensions => slice => {
  let grid = new Grid({ defaultValue: 0 });
  slice.forEach((row, y) =>
    row.forEach((v, x) => grid.set(x, y, ...Array(dimensions - 2).fill(0), v))
  );
  const deltas = directions(dimensions);

  for (let cycle = 1; cycle <= 6; cycle++) {
    const nextGrid = grid.clone();
    withNeighbors(nextGrid, deltas).forEach(coords => {
      const activeNeighbors = deltas
        .map(delta => grid.get(...coords.map((c, idx) => c + delta[idx])))
        .reduce((a, b) => a + b);

      if (
        grid.get(...coords) === 1 &&
        activeNeighbors !== 2 &&
        activeNeighbors !== 3
      ) {
        nextGrid.set(...coords, 0);
      } else if (grid.get(...coords) === 0 && activeNeighbors === 3) {
        nextGrid.set(...coords, 1);
      }
    });
    grid = nextGrid;
  }

  return [...grid.clone()].length;
};

exports.solveOne = solve(3);

exports.solveTwo = solve(4);
