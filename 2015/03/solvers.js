const dirs = { '^': [0, 1], '>': [1, 0], v: [0, -1], '<': [-1, 0] };

exports.normalizeInput = lines => [...lines[0]].map(c => dirs[c]);

const visit = directions => {
  const agent = [0, 0];
  const visited = new Set(['0,0']);

  directions.forEach(([dx, dy]) => {
    agent[0] += dx;
    agent[1] += dy;
    visited.add(agent.join(','));
  });

  return visited;
};

exports.solveOne = directions => visit(directions).size;

exports.solveTwo = directions =>
  new Set([
    ...visit(directions.filter((_, idx) => idx % 2 === 0)),
    ...visit(directions.filter((_, idx) => idx % 2 === 1)),
  ]).size;
