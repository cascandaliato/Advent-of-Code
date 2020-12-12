exports.normalizeInput = lines => [...lines[0]];

exports.solveOne = instructions =>
  instructions.map(instr => (instr === '(' ? 1 : -1)).reduce((a, b) => a + b);

exports.solveTwo = instructions => {
  let floor = 0;
  for (let i = 0; i < instructions.length; i++) {
    instructions[i] === '(' ? floor++ : floor--;
    if (floor < 0) return i + 1;
  }
};
