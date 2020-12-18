const { infixToPostfix, evaluatePostfix } = require('../../utils');

exports.normalizeInput = lines => lines;

const withPrecedence = precedence => expressions =>
  expressions
    .map(expression => evaluatePostfix(infixToPostfix(expression, precedence)))
    .reduce((a, b) => a + b);

exports.solveOne = withPrecedence({ '+': 0, '*': 0 });

exports.solveTwo = withPrecedence({ '+': 1, '*': 0 });
