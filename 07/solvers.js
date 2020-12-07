const BAGS_COLOR_RE = /^(\d?)\s?(.*?) bags?$/;

exports.normalizeInput = lines =>
  lines
    .map(l => l.slice(0, -1).split(' bags contain '))
    .reduce(
      (contains, [container, containees]) => ({
        ...contains,
        [container]:
          containees === 'no other bags'
            ? []
            : containees.split(', ').map(c => ({
                color: c.match(BAGS_COLOR_RE)[2],
                number: Number(c.match(BAGS_COLOR_RE)[1]),
              })),
      }),
      {}
    );

const containsShinyGold = contains => color =>
  +contains[color].reduce(
    (res, { color: c }) =>
      res || c === 'shiny gold' || containsShinyGold(contains)(c),
    false
  );

exports.solveOne = contains =>
  Object.keys(contains).filter(containsShinyGold(contains)).length;

const countContained = color => contains =>
  contains[color].reduce(
    (total, { color: c, number: n }) =>
      total + n * (1 + countContained(c)(contains)),
    0
  );

exports.solveTwo = countContained('shiny gold');
