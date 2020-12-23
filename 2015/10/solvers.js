const { composeN } = require('../../utils');

exports.normalizeInput = lines => lines[0];

const lookAndSay = look => {
  let say = '';

  let current = look[0];
  let count = 1;

  for (const ch of look.slice(1)) {
    if (ch === current) count++;
    else {
      say += '' + count + current;

      current = ch;
      count = 1;
    }
  }
  say += '' + count + current;
  return say;
};

exports.lookAndSay = lookAndSay;

const getLengthOfLookAndSay = times => initialValue =>
  composeN(lookAndSay, times)(initialValue).length;

exports.solveOne = getLengthOfLookAndSay(40);

exports.solveTwo = getLengthOfLookAndSay(50);
