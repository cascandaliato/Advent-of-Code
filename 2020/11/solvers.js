const { cloneDeep, isEqual } = require('lodash');

exports.normalizeInput = lines => lines.map(r => r.split(''));

const directions = [
  [0, 1],
  [0, -1],
  [1, 1],
  [1, 0],
  [1, -1],
  [-1, 1],
  [-1, 0],
  [-1, -1],
];

const numberOccupiedOne = (seats, row, col) =>
  directions.reduce((occ, [dx, dy]) => {
    const x = row + dx;
    const y = col + dy;
    if (x < 0 || x >= seats.length) return occ;
    if (y < 0 || y >= seats[0].length) return occ;
    return occ + (seats[x][y] === '#');
  }, 0);

const transform = (countOccupied, tolerance) => seats => {
  const newSeats = cloneDeep(seats);
  for (let r = 0; r < seats.length; r++) {
    for (let c = 0; c < seats[0].length; c++) {
      switch (seats[r][c]) {
        case '.':
          continue;
        case 'L':
          if (countOccupied(seats, r, c) === 0) newSeats[r][c] = '#';
          break;
        case '#':
          if (countOccupied(seats, r, c) >= tolerance) newSeats[r][c] = 'L';
          break;
      }
    }
  }
  return newSeats;
};

const solve = (countOccupied, tolerance) => seats => {
  const customTransform = transform(countOccupied, tolerance);
  let newSeats = customTransform(seats);

  while (!isEqual(newSeats, seats)) {
    seats = newSeats;
    newSeats = customTransform(seats);
  }

  return [...newSeats.join(',')].filter(c => c === '#').length;
};

exports.solveOne = solve(numberOccupiedOne, 4);

const numberOccupiedTwo = (seats, row, col) =>
  directions.reduce((occ, [dx, dy]) => {
    let x = row;
    let y = col;
    while (true) {
      x += dx;
      y += dy;
      if (x < 0 || x >= seats.length) return occ;
      if (y < 0 || y >= seats[0].length) return occ;
      switch (seats[x][y]) {
        case '.':
          continue;
        case '#':
          return occ + 1;
        case 'L':
          return occ;
      }
    }
  }, 0);

exports.solveTwo = solve(numberOccupiedTwo, 5);
