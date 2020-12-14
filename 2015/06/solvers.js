const REGEX = /(toggle|on|off) (\d+,\d+) through (\d+,\d+)/;

exports.normalizeInput = lines =>
  lines.map(line => {
    const m = line.match(REGEX);
    const [x1, y1] = m[2].split(',').map(Number);
    const [x2, y2] = m[3].split(',').map(Number);
    return {
      action: m[1],
      xStart: Math.min(x1, x2),
      yStart: Math.min(y1, y2),
      xEnd: Math.max(x1, x2),
      yEnd: Math.max(y1, y2),
    };
  });

const solve = actions => instructions => {
  const lights = Array(1000)
    .fill(0)
    .map(() => Array(1000).fill(0));

  instructions.forEach(({ action, xStart, yStart, xEnd, yEnd }) => {
    for (let x = xStart; x <= xEnd; x++) {
      for (let y = yStart; y <= yEnd; y++) {
        lights[x][y] = actions[action](lights[x][y]);
      }
    }
  });

  return lights.map(row => row.reduce((a, b) => a + b)).reduce((a, b) => a + b);
};

const actionsPartOne = { on: () => 1, off: () => 0, toggle: l => 1 - l };

exports.solveOne = solve(actionsPartOne);

const actionsPartTwo = {
  on: l => l + 1,
  off: l => Math.max(l - 1, 0),
  toggle: l => l + 2,
};

exports.solveTwo = solve(actionsPartTwo);
