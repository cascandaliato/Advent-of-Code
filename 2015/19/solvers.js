const { indicesOf, numUpper, splitByBlankLine } = require('../../utils');

exports.normalizeInput = lines => {
  const [replacements, initialValue] = splitByBlankLine(lines);
  return {
    initialValue: initialValue[0],
    replacements: replacements
      .map(replacement => replacement.split(' => '))
      // sort by decreasing number of "molecules" removed
      .sort(
        ([from1, to1], [from2, to2]) =>
          numUpper(to2) - numUpper(from2) - (numUpper(to1) - numUpper(from1))
      ),
  };
};

exports.solveOne = ({ initialValue, replacements }) =>
  new Set(
    replacements.flatMap(([from, to]) =>
      indicesOf(from, initialValue).map(index =>
        [
          ...initialValue.slice(0, index),
          ...to,
          ...initialValue.slice(index + from.length),
        ].join('')
      )
    )
  ).size;

exports.solveTwo = ({ initialValue, replacements }) => {
  if (initialValue === 'e') return 0;

  for (const [from, to] of replacements) {
    if (initialValue.indexOf(to) > -1) {
      const count = exports.solveTwo({
        initialValue: initialValue.replace(to, from),
        replacements,
      });
      if (count < +Infinity) return count + 1;
    }
  }

  return +Infinity;
};
