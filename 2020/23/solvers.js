exports.normalizeInput = lines => lines[0].split('').map(Number);

const play = (inputCups, numCups, numMoves) => {
  const cups = new Uint32Array(numCups + 1).map((_, idx) => idx + 1);
  for (let i = 0; i < inputCups.length; i++)
    cups[inputCups[i]] = inputCups[(i + 1) % inputCups.length];

  cups[0] = inputCups[0];

  if (numCups > inputCups.length) {
    cups[inputCups[inputCups.length - 1]] = inputCups.length + 1;
    cups[cups.length - 1] = inputCups[0];
  }

  for (let move = 1; move <= numMoves; move++) {
    const [p1, p2, p3] = [
      cups[cups[0]],
      cups[cups[cups[0]]],
      cups[cups[cups[cups[0]]]],
    ];
    let destination = cups[0] - 1 || numCups;
    while ([p1, p2, p3].includes(destination))
      destination = destination - 1 || numCups;

    cups[cups[0]] = cups[p3];

    cups[p3] = cups[destination];
    cups[destination] = p1;

    cups[0] = cups[cups[0]];
  }

  return cups;
};

exports.solveOne = inputCups => {
  const cups = play(inputCups, 9, 100);

  const ans = [];
  let node = cups[1];
  while (node !== 1) {
    ans.push(node);
    node = cups[node];
  }
  return Number(ans.join(''));
};

exports.solveTwo = inputCups => {
  const cups = play(inputCups, 1e6, 1e7);
  return cups[1] * cups[cups[1]];
};
