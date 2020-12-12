exports.normalizeInput = lines => lines;

exports.solveOne = strings =>
  strings
    .filter(s => /([aeiou].*){3}/.test(s))
    .filter(s => /([a-z])\1/.test(s))
    .filter(s => !/(ab|cd|pq|xy)/.test(s)).length;

exports.solveTwo = strings =>
  strings.filter(s => /(.{2}).*\1/.test(s)).filter(s => /(.).\1/.test(s))
    .length;
