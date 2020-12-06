const { splitByBlankLine } = require('../utils');

exports.parse = lines =>
  splitByBlankLine(lines).map(group => group.map(line => new Set(line)));

exports.solveOne = answers =>
  answers
    .map(group =>
      group.reduce((union, person) => new Set([...union, ...person]), new Set())
    )
    .map(union => union.size)
    .reduce((a, b) => a + b);

exports.solveTwo = answers =>
  answers
    .map(group =>
      group.reduce(
        (intersection, person) =>
          new Set([...intersection].filter(answer => person.has(answer)))
      )
    )
    .map(intersection => intersection.size)
    .reduce((a, b) => a + b);
