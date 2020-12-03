exports.parse = lines => lines.map(l => [...l]);

const downTheSlope = (right, down) => input => {
  const cols = input[0].length;
  let numTrees = 0;
  for (
    let col = 0, row = 0;
    row < input.length;
    col = (col + right) % cols, row += down
  ) {
    if (input[row][col] === '#') numTrees++;
  }
  return numTrees;
};

exports.solveOne = downTheSlope(3, 1);

exports.solveTwo = input =>
  [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
  ].reduce((acc, [right, down]) => acc * downTheSlope(right, down)(input), 1);
