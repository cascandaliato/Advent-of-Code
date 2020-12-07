const BAGS_COLOR_RE = /^(\d?)\s?(.*?) bags?$/;

exports.parse = lines =>
  lines
    .map(l => l.split(' bags contain '))
    .reduce(
      (containers, [container, containees]) => ({
        ...containers,
        [container]:
          containees === 'no other bags.'
            ? []
            : containees
                .slice(0, -1)
                .split(', ')
                .map(c => ({
                  color: c.match(BAGS_COLOR_RE)[2],
                  number: Number(c.match(BAGS_COLOR_RE)[1]),
                })),
      }),
      {}
    );

exports.solveOne = contains => {
  const isContained = Object.entries(contains).reduce(
    (acc, [container, containees]) => {
      containees.forEach(({ color }) =>
        color in acc
          ? acc[color].add(container)
          : (acc[color] = new Set([container]))
      );
      return acc;
    },
    {}
  );

  const containsShinyGold = new Set();
  const q = ['shiny gold'];
  while (q.length) {
    const color = q.pop();
    containsShinyGold.add(color);
    if (color in isContained) {
      [...isContained[color]].forEach(c => q.push(c));
    }
  }
  return [...containsShinyGold].filter(c => c !== 'shiny gold').length;
};

exports.solveTwo = contains => {
  const bagsInColor = {};

  const q = ['shiny gold'];
  while (q.length) {
    const color = q.pop();
    if (contains[color].every(({ color: c }) => c in bagsInColor)) {
      bagsInColor[color] = contains[color].reduce(
        (count, { number: n, color: c }) => count + n + n * bagsInColor[c],
        0
      );
    } else {
      q.push(color);
      contains[color].forEach(({ color: c }) => q.push(c));
    }
  }

  return bagsInColor['shiny gold'];
};
