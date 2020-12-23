const { permutations } = require('../../utils');

exports.normalizeInput = lines =>
  lines.reduce((distances, line) => {
    const [fromTo, distance] = line.split(' = ');
    const [from, to] = fromTo.split(' to ');

    if (!(from in distances)) distances[from] = {};
    distances[from][to] = Number(distance);

    if (!(to in distances)) distances[to] = {};
    distances[to][from] = Number(distance);

    return distances;
  }, {});

const allPaths = distances =>
  [...permutations(Object.keys(distances))].map(path =>
    path
      .slice(0, -1)
      .reduce(
        (distance, from, idx) => distance + distances[from][path[idx + 1]],
        0
      )
  );

exports.solveOne = distances =>
  allPaths(distances).reduce((a, b) => Math.min(a, b));

exports.solveTwo = distances =>
  allPaths(distances).reduce((a, b) => Math.max(a, b));
