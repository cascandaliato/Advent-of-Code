const { rotateCW: rCW, rotateCCW: rCCW, repeatFn } = require('../utils');

exports.normalizeInput = lines =>
  lines.map(line => ({ action: line[0], value: Number(line.slice(1)) }));

const rotateCW = (px, py, val) => repeatFn(rCW, val / 90)([px, py]);
const rotateCCW = (px, py, val) => repeatFn(rCCW, val / 90)([px, py]);

const navigate = (navigationSystem, initialState) => instructions => {
  const { x, y } = instructions.reduce(
    (state, { action, value }) => navigationSystem[action](state, value),
    initialState
  );
  return Math.abs(x) + Math.abs(y);
};

const navigationPartOne = {
  N: (state, val) => ({ ...state, y: state.y + val }),
  S: (state, val) => ({ ...state, y: state.y - val }),
  E: (state, val) => ({ ...state, x: state.x + val }),
  W: (state, val) => ({ ...state, x: state.x - val }),
  L: (state, val) => ({
    ...state,
    dx: rotateCCW(state.dx, state.dy, val)[0],
    dy: rotateCCW(state.dx, state.dy, val)[1],
  }),
  R: (state, val) => ({
    ...state,
    dx: rotateCW(state.dx, state.dy, val)[0],
    dy: rotateCW(state.dx, state.dy, val)[1],
  }),
  F: (state, val) => ({
    ...state,
    x: state.x + val * state.dx,
    y: state.y + val * state.dy,
  }),
};

exports.solveOne = navigate(navigationPartOne, { x: 0, y: 0, dx: 1, dy: 0 });

const navigationPartTwo = {
  N: (state, val) => ({ ...state, wy: state.wy + val }),
  S: (state, val) => ({ ...state, wy: state.wy - val }),
  E: (state, val) => ({ ...state, wx: state.wx + val }),
  W: (state, val) => ({ ...state, wx: state.wx - val }),
  L: (state, val) => ({
    ...state,
    wx: rotateCCW(state.wx, state.wy, val)[0],
    wy: rotateCCW(state.wx, state.wy, val)[1],
  }),
  R: (state, val) => ({
    ...state,
    wx: rotateCW(state.wx, state.wy, val)[0],
    wy: rotateCW(state.wx, state.wy, val)[1],
  }),
  F: (state, val) => ({
    ...state,
    x: state.x + val * state.wx,
    y: state.y + val * state.wy,
  }),
};

exports.solveTwo = navigate(navigationPartTwo, { x: 0, y: 0, wx: 10, wy: 1 });
