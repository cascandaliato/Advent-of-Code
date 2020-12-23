class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
    this.down = null;
  }
}

const buildLinks = cups => {
  const maxCup = cups.reduce((a, b) => Math.max(a, b));
  const byValue = new Map(cups.map(cup => [cup, new Node(cup)]));

  for (const [value, node] of byValue) {
    const down = value - 1 || maxCup;
    node.down = byValue.get(down);
  }

  cups.slice(1, -1).forEach((cup, idx) => {
    byValue.get(cup).next = byValue.get(cups[idx + 1 + 1]);
    byValue.get(cup).prev = byValue.get(cups[idx + 1 - 1]);
  });

  byValue.get(cups[0]).next = byValue.get(cups[1]);
  byValue.get(cups[0]).prev = byValue.get(cups[cups.length - 1]);
  byValue.get(cups[cups.length - 1]).next = byValue.get(cups[0]);
  byValue.get(cups[cups.length - 1]).prev = byValue.get(cups[cups.length - 2]);

  return { current: byValue.get(cups[0]), one: byValue.get(1) };
};

exports.normalizeInput = lines =>
  lines.map(line => line.split('').map(Number))[0];

const playWithCupsAndMoves = (numCups, moves) => cups => {
  for (let cup = 10; cup <= numCups; cup++) cups.push(cup);
  let { current, one } = buildLinks(cups);

  for (let move = 1; move <= moves; move++) {
    const [p1, p2, p3] = [
      current.next,
      current.next.next,
      current.next.next.next,
    ];
    let destination = current.down;
    while ([p1.value, p2.value, p3.value].includes(destination.value))
      destination = destination.down;

    current.next = p3.next;
    p3.next.prev = current;

    p3.next = destination.next;
    destination.next.prev = p3;
    destination.next = p1;
    p1.prev = destination;

    current = current.next;
  }

  return one;
};

exports.solveOne = cups => {
  const one = playWithCupsAndMoves(9, 100)(cups);

  let node = one.next;
  const answer = [];
  while (node.value !== 1) {
    answer.push(node.value);
    node = node.next;
  }
  return Number(answer.join(''));
};

exports.solveTwo = cups => {
  const one = playWithCupsAndMoves(1e6, 1e7)(cups);
  return one.next.value * one.next.next.value;
};
