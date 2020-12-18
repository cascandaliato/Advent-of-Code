const { combos } = require('../../utils');
const HyperCounter = require('../../utils/hyper-counter');
const HyperSet = require('../../utils/hyper-set');

const status = { '#': 1, '.': 0 };

exports.normalizeInput = lines =>
  lines.map(line => [...line].map(ch => status[ch]));

const directions = dimensions =>
  combos([0, -1, 1], dimensions).filter(combo => !combo.every(v => v === 0));

const solve = ({ dimensions, generations }) => slice => {
  let cube = new HyperSet();

  const lengths = [
    slice[0].length + generations * 2,
    slice.length + generations * 2,
    ...Array(dimensions - 2).fill(1 + generations * 2),
  ];

  slice.forEach((row, y) =>
    row.forEach(
      (v, x) =>
        v === 1 &&
        cube.add([
          x + generations,
          y + generations,
          ...Array(dimensions - 2).fill(generations),
        ])
    )
  );

  const deltas = directions(dimensions);

  for (let cycle = 1; cycle <= generations; cycle++) {
    const nextCube = new HyperSet();

    const counter = new HyperCounter();
    [...cube].forEach(coords =>
      deltas
        .map(delta => coords.map((c, idx) => c + delta[idx]))
        .filter(c => c.every((v, idx) => v >= 0 && v < lengths[idx]))
        .forEach(c => counter.add(c))
    );

    for (const [coords, value] of counter) {
      if (value === 3 || (value === 2 && cube.has(coords))) {
        nextCube.add(coords);
      }
    }

    cube = nextCube;
  }

  return cube.getPopulated().length;
};

exports.solveOne = solve({ dimensions: 3, generations: 6 });

exports.solveTwo = solve({ dimensions: 4, generations: 6 });
