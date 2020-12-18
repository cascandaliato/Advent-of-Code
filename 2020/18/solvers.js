// const { infixToPostfix, evaluatePostfix } = require('../../utils');

// exports.normalizeInput = lines => lines;

// const withPrecedence = precedence => expressions =>
//   expressions
//     .map(expression => evaluatePostfix(infixToPostfix(expression, precedence)))
//     .reduce((a, b) => a + b);

// exports.solveOne = withPrecedence({ '+': 0, '*': 0 });

// exports.solveTwo = withPrecedence({ '+': 1, '*': 0 });

// ---

exports.normalizeInput = lines =>
  lines.map(expression => expression.replace(/\s+/g, ''));

const applyRepeatedly = ops => expressions =>
  expressions
    .map(expression => {
      while (!/^\d+$/.test(expression)) {
        for (const { regex, op } of ops) {
          const match = expression.match(regex);
          if (match) {
            expression = expression.replace(regex, op(match));
            break;
          }
        }
      }
      return Number(expression);
    })
    .reduce((a, b) => a + b);

const opsPartOne = [
  { regex: /\((\d+)\)/, op: m => m[1] },
  { regex: /^(\d+)\+(\d+)/, op: m => Number(m[1]) + Number(m[2]) },
  { regex: /\((\d+)\+(\d+)/, op: m => '(' + (Number(m[1]) + Number(m[2])) },
  { regex: /^(\d+)\*(\d+)/, op: m => Number(m[1]) * Number(m[2]) },
  { regex: /\((\d+)\*(\d+)/, op: m => '(' + Number(m[1]) * Number(m[2]) },
];

exports.solveOne = applyRepeatedly(opsPartOne);

const opsPartTwo = [
  { regex: /\((\d+)\)/, op: m => m[1] },
  { regex: /(\d+)\+(\d+)/, op: m => Number(m[1]) + Number(m[2]) },
  { regex: /\((\d+)\*(\d+)\)/, op: m => Number(m[1]) * Number(m[2]) },
  { regex: /(\d+)\*(\d+)/, op: m => Number(m[1]) * Number(m[2]) },
];

exports.solveTwo = applyRepeatedly(opsPartTwo);
