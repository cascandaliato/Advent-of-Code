const fs = require('fs');
const { flow, range, zip } = require('lodash');

exports.readFileLines = path => fs.readFileSync(path).toString().split('\n');

exports.splitByBlankLine = lines =>
  lines
    .join('\n')
    .split('\n\n')
    .map(g => g.split('\n'));

exports.tests = (suite, fn, tests) => {
  describe(suite, () => {
    let id = 0;
    tests.forEach(({ input, expectedOutput }) => {
      test(`#${++id}`, async () => {
        expect(await fn(input)).toBe(expectedOutput);
      });
    });
  });
};

// fn = continuation => args => {}
// and args must be JSON-serializable
exports.memoizeRecursive = (fn, baseCase) => {
  const memo = new Map();
  if (baseCase) memo.set(JSON.stringify([baseCase.in]), baseCase.out);

  const memoized = (...args) => {
    const key = JSON.stringify(args);
    if (!memo.has(key)) memo.set(key, fn(memoized)(...args));
    return memo.get(key);
  };

  return memoized;
};

exports.memoize = fn => exports.memoizeRecursive(() => fn);

exports.mod = (n, mod) => ((n % mod) + mod) % mod;

const rotate = dir => ([px, py]) => [dir * py, -dir * px];
exports.rotateCW = rotate(1);
exports.rotateCCW = rotate(-1);

exports.repeatFn = (fn, times) => flow(...range(times).fill(fn));

// https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
exports.extendedEuclidean = (a, b) => {
  let [prevR, r] = [a, b];
  let [prevS, s] = [1, 0];
  let [prevT, t] = [0, 1];
  while (r !== 0) {
    const q = Math.floor(prevR / r);
    [prevR, r] = [r, prevR - q * r];
    [prevS, s] = [s, prevS - q * s];
    [prevT, t] = [t, prevT - q * t];
  }
  return [prevS, prevT, prevR];
};

exports.gcd = (...numbers) => {
  if (numbers.length === 2) {
    return exports.extendedEuclidean(...numbers)[2];
  } else {
    return exports.gcd(numbers[0], exports.gcd(...numbers.slice(1)));
  }
};

// https://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm
const modInv = (a, b) => exports.mod(exports.extendedEuclidean(a, b)[0], b);

// https://rosettacode.org/wiki/Chinese_remainder_theorem
exports.chineseRemainder = (moduli, remainders) => {
  let sum = 0;
  const product = moduli.reduce((a, b) => a * b);
  for (const [modulus, remainder] of zip(moduli, remainders)) {
    const p = product / modulus;
    sum += remainder * modInv(p, modulus) * p;
  }
  return sum % product;
};

exports.combos = (elements, times) =>
  times === 1
    ? elements.map(e => [e])
    : elements.flatMap(e =>
        exports.combos(elements, times - 1).map(c => [e, ...c])
      );

exports.multiRange = boundaries =>
  boundaries.length === 1
    ? range(boundaries[0][0], boundaries[0][1] + 1).map(v => [v])
    : exports
        .multiRange(boundaries.slice(1))
        .flatMap(mr =>
          range(boundaries[0][0], boundaries[0][1] + 1).map(v => [v, ...mr])
        );

// https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#JavaScript
// https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail
exports.infixToPostfix = (
  infix,
  precedence = { '^': 4, '*': 3, '/': 3, '+': 2, '-': 2 }
) => {
  infix = infix.replace(/\s+/g, '');

  const ops = '-+/*^';
  const associativity = {
    '^': 'Right',
    '*': 'Left',
    '/': 'Left',
    '+': 'Left',
    '-': 'Left',
  };

  const operators = [];
  const postfix = [];

  let token;
  let op1, op2;

  for (let i = 0; i < infix.length; i++) {
    token = infix[i];
    if (token >= '0' && token <= '9') {
      let j = i + 1;
      while (infix[j] >= '0' && infix[j] <= '9') {
        token += infix[j];
        j++;
      }
      i = j - 1;
      postfix.push(Number(token));
    } else if (ops.indexOf(token) != -1) {
      op1 = token;
      op2 = operators[operators.length - 1];
      while (
        ops.indexOf(op2) != -1 &&
        ((associativity[op1] == 'Left' && precedence[op1] <= precedence[op2]) ||
          (associativity[op1] == 'Right' && precedence[op1] < precedence[op2]))
      ) {
        postfix.push(operators.pop());
        op2 = operators[operators.length - 1];
      }
      operators.push(op1);
    } else if (token == '(') {
      operators.push(token);
    } else if (token == ')') {
      while (operators[operators.length - 1] != '(') {
        postfix.push(operators.pop());
      }
      operators.pop();
    }
  }
  postfix.push(...operators.reverse());
  return postfix;
};

exports.evaluatePostfix = postfix => {
  const input = [...postfix];

  const ops = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => a / b,
    '^': (a, b) => a ^ b,
  };

  const operands = [];
  while (input.length > 0) {
    const token = input.shift();
    if (token in ops) {
      operands.push(ops[token](operands.pop(), operands.pop()));
    } else {
      operands.push(token);
    }
  }

  return operands[0];
};

exports.memoize = fn => {
  const cache = new Map();
  return (...args) => {
    const key = JSON.stringify(args);
    if (!cache.has(key)) cache.set(key, fn(...args));
    return cache.get(key);
  };
};

exports.printMatrixWithMap = (map = {}) => (matrix, id = undefined) => {
  console.log();
  if (id) console.log(`[id=${id}]`);
  for (const row of matrix) {
    console.log(row.map(c => map[c] || c).join(''));
  }
  console.log();
};

exports.printMatrix = exports.printMatrixWithMap();

exports.getCol = (matrix, idx) =>
  matrix.reduce((col, row) => [...col, row[idx]], []);

exports.permutations = function* (elements) {
  if (elements.length === 1) yield elements;

  for (const element of elements) {
    for (const rest of exports.permutations(
      elements.filter(e => e !== element)
    )) {
      yield [element, ...rest];
    }
  }
};

exports.numberPartitions = function* (target, numParts) {
  if (numParts === 1) yield [target];
  else
    for (let i = 0; i <= target; i++)
      for (const rest of exports.numberPartitions(target - i, numParts - 1))
        yield [i, ...rest];
};

exports.composeN = (fn, n = 1) => (...args) =>
  n === 1 ? fn(...args) : exports.composeN(fn, n - 1)(fn(...args));

exports.toMatrix = lines => lines.map(line => line.split(''));

exports.getDimensions = hypercube =>
  Array.isArray(hypercube) ? 1 + exports.getDimensions(hypercube[0]) : 0;

exports.getLengths = hypercube =>
  exports.getDimensions(hypercube) === 1
    ? [hypercube.length]
    : [hypercube.length, ...exports.getLengths(hypercube[0])];

exports.getDirections = (n = 2) =>
  exports.combos([0, 1, -1], n).filter(combo => combo.some(v => v !== 0));
