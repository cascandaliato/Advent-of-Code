exports.normalizeInput = lines => JSON.parse(lines[0]);

exports.solveOne = json =>
  (JSON.stringify(json).match(/(-?\d+)/g) || [])
    .map(Number)
    .reduce((a, b) => a + b, 0);

exports.solveTwo = thing => {
  switch (typeof thing) {
    case 'number':
      return thing;
    case 'string':
      return 0;
    case 'object':
      if (Array.isArray(thing))
        return thing.reduce((sum, sub) => sum + exports.solveTwo(sub), 0);
      else if (!Object.values(thing).includes('red'))
        return Object.values(thing).reduce(
          (sum, sub) => sum + exports.solveTwo(sub),
          0
        );
      else return 0;
  }
};
