exports.normalizeInput = lines =>
  lines.map(line =>
    line
      .split('x')
      .map(Number)
      .sort((a, b) => a - b)
  );

exports.solveOne = dimensions =>
  dimensions
    .map(([w, h, l]) => w * h + 2 * l * w + 2 * w * h + 2 * h * l)
    .reduce((a, b) => a + b);

exports.solveTwo = dimensions =>
  dimensions
    .map(([w, h, l]) => 2 * (w + h) + w * h * l)
    .reduce((a, b) => a + b);
