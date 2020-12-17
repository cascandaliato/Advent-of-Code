const { combos } = require('../../utils');
const HyperCube = require('../../utils/hyper-cube');

const status = { '#': 1, '.': 0 };

exports.normalizeInput = lines =>
  lines.map(line => [...line].map(ch => status[ch]));

const directions = dimensions =>
  combos([0, -1, 1], dimensions).filter(combo => !combo.every(v => v === 0));

const withNeighbors = (grid, deltas) =>
  [
    ...new Set([
      ...[...grid.entries()].map(([coords]) => coords.join(',')),
      ...[...grid.entries()]
        .flatMap(([coords]) =>
          deltas.map(delta => delta.map((d, idx) => d + coords[idx]))
        )
        .map(arr => arr.join(',')),
    ]),
  ]
    .map(str => str.split(',').map(Number))
    .filter(coords =>
      coords.every((coord, idx) => coord >= 0 && coord < grid.lengths[idx])
    );

const solve = ({ dimensions, generations }) => slice => {
  let cube = new HyperCube({
    lengths: [
      slice[0].length + generations * 2,
      slice.length + generations * 2,
      ...Array(dimensions - 2).fill(1 + generations * 2),
    ],
    defaultValue: 0,
  });
  slice.forEach((row, y) =>
    row.forEach((v, x) =>
      cube.set(
        x + generations,
        y + generations,
        ...Array(dimensions - 2).fill(generations),
        v
      )
    )
  );

  const deltas = directions(dimensions);
  for (let cycle = 1; cycle <= generations; cycle++) {
    const nextCube = cube.clone();
    withNeighbors(nextCube, deltas).forEach(coords => {
      const activeNeighbors = deltas
        .map(delta => coords.map((c, idx) => c + delta[idx]))
        .filter(c => c.every((v, idx) => v >= 0 && v < cube.lengths[idx]))
        .map(c => cube.get(...c))
        .reduce((a, b) => a + b);

      if (
        cube.get(...coords) === 1 &&
        activeNeighbors !== 2 &&
        activeNeighbors !== 3
      ) {
        nextCube.set(...coords, 0);
      } else if (cube.get(...coords) === 0 && activeNeighbors === 3) {
        nextCube.set(...coords, 1);
      }
    });
    cube = nextCube;
  }

  return cube.getPopulated().length;
};

exports.solveOne = solve({ dimensions: 3, generations: 6 });

exports.solveTwo = solve({ dimensions: 4, generations: 6 });
