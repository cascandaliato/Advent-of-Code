const { mod } = require('../../utils');

exports.normalizeInput = lines => lines[0].split('').map(Number);

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null;
    this.down = null;
  }
}

const buildLinks = cups => {
  const byValue = new Map(cups.map(cup => [cup, new Node(cup)]));

  for (const [value, node] of byValue)
    node.down = byValue.get(value - 1 || cups.length);

  cups.forEach((cup, idx) => {
    byValue.get(cup).next = byValue.get(cups[mod(idx + 1, cups.length)]);
    byValue.get(cup).prev = byValue.get(cups[mod(idx - 1, cups.length)]);
  });

  return { current: byValue.get(cups[0]), one: byValue.get(1) };
};

const play = (numCups, numMoves) => cups => {
  for (let cup = 10; cup <= numCups; cup++) cups.push(cup);
  let { current, one } = buildLinks(cups);

  for (let move = 1; move <= numMoves; move++) {
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
  const one = play(9, 100)(cups);

  let node = one.next;
  const answer = [];
  while (node.value !== 1) {
    answer.push(node.value);
    node = node.next;
  }
  return Number(answer.join(''));
};

exports.solveTwo = cups => {
  const one = play(1e6, 1e7)(cups);
  return one.next.value * one.next.next.value;
};
