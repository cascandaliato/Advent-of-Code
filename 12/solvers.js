exports.normalizeInput = lines =>
  lines.map(line => ({ action: line[0], value: Number(line.slice(1)) }));

const rotate = dir => (px, py, val) =>
  Array(val / 90)
    .fill(0)
    .reduce(([a, b]) => [dir * b, -dir * a], [px, py]);

const rotateCW = rotate(1);
const rotateCCW = rotate(-1);

const navigate = (navigationSystem, initialState) => instructions => {
  const { x, y } = instructions.reduce(
    (state, { action, value }) => navigationSystem[action](state, value),
    initialState
  );
  return Math.abs(x) + Math.abs(y);
};

const navigationPartOne = {
  N: ({ x, y, dx, dy }, val) => ({ x, y: y + val, dx, dy }),
  S: ({ x, y, dx, dy }, val) => ({ x, y: y - val, dx, dy }),
  E: ({ x, y, dx, dy }, val) => ({ x: x + val, y, dx, dy }),
  W: ({ x, y, dx, dy }, val) => ({ x: x - val, y, dx, dy }),
  L: ({ x, y, dx, dy }, val) => ({
    x,
    y,
    dx: rotateCCW(dx, dy, val)[0],
    dy: rotateCCW(dx, dy, val)[1],
  }),
  R: ({ x, y, dx, dy }, val) => ({
    x,
    y,
    dx: rotateCW(dx, dy, val)[0],
    dy: rotateCW(dx, dy, val)[1],
  }),
  F: ({ x, y, dx, dy }, val) => ({
    x: x + val * dx,
    y: y + val * dy,
    dx,
    dy,
  }),
};

exports.solveOne = navigate(navigationPartOne, { x: 0, y: 0, dx: 1, dy: 0 });

const navigationPartTwo = {
  N: ({ x, y, wx, wy }, val) => ({ x, y, wx, wy: wy + val }),
  S: ({ x, y, wx, wy }, val) => ({ x, y, wx, wy: wy - val }),
  E: ({ x, y, wx, wy }, val) => ({ x, y, wx: wx + val, wy }),
  W: ({ x, y, wx, wy }, val) => ({ x, y, wx: wx - val, wy }),
  L: ({ x, y, wx, wy }, val) => ({
    x,
    y,
    wx: rotateCCW(wx, wy, val)[0],
    wy: rotateCCW(wx, wy, val)[1],
  }),
  R: ({ x, y, wx, wy }, val) => ({
    x,
    y,
    wx: rotateCW(wx, wy, val)[0],
    wy: rotateCW(wx, wy, val)[1],
  }),
  F: ({ x, y, wx, wy }, val) => ({ x: x + val * wx, y: y + val * wy, wx, wy }),
};

exports.solveTwo = navigate(navigationPartTwo, { x: 0, y: 0, wx: 10, wy: 1 });
