exports.normalizeInput = lines => lines;

exports.solveOne = lines =>
  lines.map(line => line.length).reduce((a, b) => a + b) -
  lines
    .map(
      line =>
        line
          .slice(1, -1)
          .replace(/\\\\/g, '*')
          .replace(/\\"/g, '*')
          .replace(/\\x../g, '*').length
    )
    .reduce((a, b) => a + b);

exports.solveTwo = lines =>
  lines
    .map(line => line.replace(/\\/g, '\\\\').replace(/"/g, '\\"').length + 2)
    .reduce((a, b) => a + b) -
  lines.map(line => line.length).reduce((a, b) => a + b);
