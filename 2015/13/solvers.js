const { mod, permutations } = require('../../utils');

exports.normalizeInput = lines =>
  lines
    .map(line => line.slice(0, -1).split(' '))
    .map(tokens => ({
      who: tokens[0],
      neighbor: tokens[tokens.length - 1],
      change: Number(`${tokens[2] === 'gain' ? '+' : '-'}${tokens[3]}`),
    }))
    .reduce((map, { who, neighbor, change }) => {
      if (!(who in map)) map[who] = {};
      map[who][neighbor] = change;
      return map;
    }, {});

exports.solveOne = happiness =>
  [...permutations(Object.keys(happiness))]
    .map(permutation =>
      permutation
        .map(
          (guest, idx) =>
            happiness[guest][permutation[mod(idx + 1, permutation.length)]] +
            happiness[guest][permutation[mod(idx - 1, permutation.length)]]
        )
        .reduce((a, b) => a + b)
    )
    .reduce((a, b) => Math.max(a, b));

exports.solveTwo = happiness => {
  happiness['me'] = {};
  Object.keys(happiness).forEach(guest => {
    happiness[guest]['me'] = 0;
    happiness['me'][guest] = 0;
  });
  return exports.solveOne(happiness);
};
