const { fromPairs, mapValues, toPairs } = require('lodash');

exports.normalizeInput = lines =>
  lines.map(line =>
    mapValues(
      fromPairs(
        line
          .replace(/Sue \d+: /g, '')
          .split(', ')
          .map(thing => thing.split(': '))
      ),
      Number
    )
  );

const reqs = {
  children: ['eq', 3],
  cats: ['gt', 7],
  samoyeds: ['eq', 2],
  pomeranians: ['lt', 3],
  akitas: ['eq', 0],
  vizslas: ['eq', 0],
  goldfish: ['lt', 5],
  trees: ['gt', 3],
  cars: ['eq', 2],
  perfumes: ['eq', 1],
};

const ops = {
  eq: (a, b) => a === b,
  gt: (a, b) => a > b,
  lt: (a, b) => a < b,
};

const findAunt = matchPredicate => aunts => {
  for (let i = 0; i < aunts.length; i++)
    if (toPairs(aunts[i]).every(([thing, qty]) => matchPredicate(thing, qty)))
      return i + 1;
};

exports.solveOne = findAunt((thing, qty) => reqs[thing][1] === qty);

exports.solveTwo = findAunt((thing, qty) => {
  const [op, target] = reqs[thing];
  return ops[op](qty, target);
});
