const { memoize } = require('../../utils');

const parse = str => (/^\d+$/.test(str) ? Number(str) : str);

exports.normalizeInput = lines =>
  lines.reduce((wires, line) => {
    const [signal, wire] = line.split(' -> ');
    const signalTokens = signal.split(' ');
    switch (signalTokens.length) {
      case 1:
        wires[wire] = {
          type: 'literal',
          payload: [parse(signalTokens[0])],
        };
        break;
      case 2:
        wires[wire] = {
          type: signalTokens[0],
          payload: [parse(signalTokens[1])],
        };
        break;
      case 3:
        wires[wire] = {
          type: signalTokens[1],
          payload: [parse(signalTokens[0]), parse(signalTokens[2])],
        };
        break;
    }
    return wires;
  }, {});

const ops = {
  literal: ([a]) => a,
  NOT: ([a]) => ((1 << 16) - 1) ^ a,
  AND: ([a, b]) => a & b,
  OR: ([a, b]) => a | b,
  LSHIFT: ([a, n]) => a << n,
  RSHIFT: ([a, n]) => a >> n,
};

const resolveWire = memoize((wire, wires) => {
  const { type, payload } = wires[wire];
  return ops[type](
    payload.map(v => (typeof v === 'number' ? v : resolveWire(v, wires)))
  );
});

exports.solveOne = wires => resolveWire('a', wires);

exports.solveTwo = wires => {
  wires['b'] = { type: 'literal', payload: [resolveWire('a', wires)] };
  return resolveWire('a', wires);
};
