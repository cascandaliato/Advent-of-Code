const MASK = /^mask = ([X01]{36})$/;
const MEM = /^mem\[(\d+)\] = (\d+)$/;

exports.normalizeInput = lines =>
  lines.map(line => {
    if (line.match(MASK)) {
      return {
        op: 'mask',
        mask: line.match(MASK)[1],
      };
    } else {
      const [address, value] = line.match(MEM).slice(1);
      return {
        op: 'mem',
        address: BigInt(address),
        value: BigInt(value),
      };
    }
  });

exports.solveOne = ops => {
  const map = new Map();
  let and, or;
  ops.forEach(op => {
    if (op.op === 'mask') {
      const { mask } = op;
      and = BigInt(parseInt(mask.replace(/X/g, '1'), 2));
      or = BigInt(parseInt(mask.replace(/X/g, '0'), 2));
    } else {
      const { address, value } = op;
      map.set(address, (value & and) | or);
    }
  });
  return Number([...map.values()].reduce((a, b) => a + b));
};

exports.solveTwo = ops => {
  const map = new Map();
  let mask;
  ops.forEach(op => {
    if (op.op === 'mask') {
      mask = op.mask;
    } else {
      const { address: originalAddress, value } = op;
      const wildcards = [];
      let addresses = [
        [...originalAddress.toString(2).padStart(36, '0')]
          .map((c, idx) => {
            if (mask[idx] === '0') {
              return c;
            } else if (mask[idx] === '1') {
              return 1;
            } else {
              wildcards.push(idx);
              return 'X';
            }
          })
          .join(''),
      ];
      let newAddresses = [];
      for (const i of wildcards) {
        for (const address of addresses) {
          newAddresses.push(
            [...address.slice(0, i), '0', ...address.slice(i + 1)].join('')
          );
          newAddresses.push(
            [...address.slice(0, i), '1', ...address.slice(i + 1)].join('')
          );
        }
        addresses = newAddresses;
        newAddresses = [];
      }
      for (const address of addresses) {
        map.set(parseInt(address, 2), value);
      }
    }
  });
  return Number([...map.values()].reduce((a, b) => a + b));
};
