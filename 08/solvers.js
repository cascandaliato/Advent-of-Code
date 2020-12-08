const ops = {
  nop: (_, idx, acc) => ({ idx: idx + 1, acc }),
  acc: (arg, idx, acc) => ({ idx: idx + 1, acc: acc + arg }),
  jmp: (arg, idx, acc) => ({ idx: idx + arg, acc }),
};

exports.normalizeInput = lines =>
  lines
    .map(line => line.split(' '))
    .map(([op, arg]) => ({ op, arg: Number(arg) }));

const execute = instructions => {
  const seen = new Set();
  let idx = 0;
  let acc = 0;
  while (!seen.has(idx)) {
    seen.add(idx);
    const { op, arg } = instructions[idx];
    ({ idx, acc } = ops[op](arg, idx, acc));
    if (idx === instructions.length) return { completed: true, acc };
  }
  return { completed: false, acc };
};

exports.solveOne = instructions => execute(instructions).acc;

exports.solveTwo = instructions => {
  const swap = { nop: 'jmp', jmp: 'nop' };

  for (const instruction of instructions.filter(({ op }) => op in swap)) {
    instruction.op = swap[instruction.op];
    const { completed, acc } = execute(instructions);
    if (completed) return acc;
    instruction.op = swap[instruction.op];
  }
};
