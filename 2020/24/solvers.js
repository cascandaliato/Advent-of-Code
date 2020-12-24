const BinaryGrid = require('../../utils/hyper-set');
const Counter = require('../../utils/hyper-counter');

const directions = {
  e: [0, 1],
  se: [1, 0],
  sw: [1, -1],
  w: [0, -1],
  nw: [-1, 0],
  ne: [-1, 1],
};

exports.normalizeInput = lines =>
  lines.map(line => {
    const dirs = [];
    let direction = '';
    for (const ch of line) {
      direction += ch;
      if (direction in directions) {
        dirs.push(direction);
        direction = '';
      }
    }
    return dirs;
  });

const followInstructions = instructions => {
  const grid = new BinaryGrid(); // include only black-side-ups
  for (const instruction of instructions) {
    let current = [0, 0];
    for (const direction of instruction) {
      current = [
        current[0] + directions[direction][0],
        current[1] + directions[direction][1],
      ];
    }
    grid.toggle(current);
  }
  return grid;
};

exports.solveOne = instructions => followInstructions(instructions).size;

exports.solveTwo = instructions => {
  let grid = followInstructions(instructions);

  // game of life
  for (let day = 1; day <= 100; day++) {
    const nextGrid = new BinaryGrid();

    const counter = new Counter();
    [...grid].forEach(coords =>
      Object.values(directions)
        .map(delta => coords.map((c, idx) => c + delta[idx]))
        .forEach(c => counter.add(c))
    );

    for (const [coords, value] of counter) {
      if (value === 2 || (value === 1 && grid.has(coords))) {
        nextGrid.add(coords);
      }
    }

    grid = nextGrid;
  }

  return grid.size;
};
