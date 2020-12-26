const { groupBy, mapValues } = require('lodash');

const HyperMap = require('./hyper-map');
const HyperSet = require('./hyper-set');
const u = require('.');

const matrixToState = matrix =>
  matrix.flatMap((row, rowIdx) =>
    row.map((state, colIdx) => [[rowIdx, colIdx], state])
  );

const lengthsToLimits = lengths => lengths.map(length => [-1, length]);

const fromLimitsArray = limits => coords =>
  limits.every(([min, max], idx) => coords[idx] > min && coords[idx] < max);

const neighborsFromDirections = directions => coords =>
  directions.map(direction => direction.map((v, idx) => v + coords[idx]));

const createAutomaton = function* ({
  cell: { defaultState, states },
  initialState, // [coords,state][]
  getNeighbors, // coords => coords[]
  isWithinLimits, // coords => bool
}) {
  let grid = new HyperMap(defaultState);
  for (const [coords, state] of initialState) grid.set(coords, state);

  const getNeighborsWithinLimits = coords =>
    getNeighbors(coords).filter(isWithinLimits);

  while (true) {
    let expanded = new HyperSet();
    [...grid].forEach(([coords]) => {
      expanded.add(coords);
      getNeighborsWithinLimits(coords).forEach(nCoords =>
        expanded.add(nCoords)
      );
    });

    const newGrid = new HyperMap(defaultState);
    [...expanded].forEach(coords => {
      const neighborsLocal = getNeighborsWithinLimits(coords).map(nCoords => [
        nCoords,
        grid.get(nCoords),
      ]);
      const byState = mapValues(
        groupBy(neighborsLocal, ([_, state]) => state),
        values => values.map(([nCoords]) => nCoords)
      );
      for (const state in states) {
        if (!(state in byState)) byState[state] = [];
      }
      const newState = states[grid.get(coords)](
        coords,
        neighborsLocal,
        byState
      );
      newGrid.set(coords, newState);
    });
    grid = newGrid;

    yield newGrid;
  }
};

const conwayFinite = ({ alive, dead, overrides = {} }) => matrix =>
  conwayInfinite({
    alive,
    dead,
    overrides: {
      ...overrides,
      isWithinLimits: fromLimitsArray(lengthsToLimits(u.getLengths(matrix))),
    },
  })(matrix);

const conwayInfinite = ({ alive, dead, overrides = {} }) => matrix =>
  createAutomaton({
    cell: {
      defaultState: dead,
      states: {
        [alive]: (_, nEntries) =>
          [2, 3].includes(countEntriesByState(nEntries, alive)) ? alive : dead,
        [dead]: (_, nEntries) =>
          countEntriesByState(nEntries, alive) === 3 ? alive : dead,
      },
    },
    initialState: matrixToState(matrix),
    getNeighbors: neighborsFromDirections(
      u.getDirections(u.getDimensions(matrix))
    ),
    isWithinLimits: () => true,
    ...overrides,
  });

const evolve = nth => automaton => {
  let generation;
  for (let i = 1; i <= nth; i++) generation = automaton.next();
  return generation.value;
};

const countEntriesByState = (entries, targetState) =>
  entries.filter(([_, state]) => state === targetState).length;

const countByState = targetState => automaton =>
  countEntriesByState([...automaton], targetState);

module.exports = {
  conwayFinite,
  countByState,
  countEntriesByState,
  evolve,
  neighborsFromDirections,
  fromLimitsArray,
  matrixToState,
};
