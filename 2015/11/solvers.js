exports.normalizeInput = lines => [...lines[0]].reverse();

const hasIncreasingSequence = password =>
  password
    .slice(0, -3)
    .some(
      (c, idx) =>
        c.charCodeAt(0) - 1 === password[idx + 1].charCodeAt(0) &&
        c.charCodeAt(0) - 2 === password[idx + 2].charCodeAt(0)
    );

const hasNoForbiddenLetters = password =>
  ['i', 'o', 'l'].every(c => !password.includes(c));

const hasTwoPairs = password =>
  new Set(
    password
      .slice(0, -1)
      .map((c, idx) => `${c}${password[idx + 1]}`)
      .filter(str => str[0] === str[1])
  ).size >= 2;

const letters = 'abcdefghijklmnopqrstuvwxyz';

const nextLetter = [...letters].reduce((map, ch, idx) => {
  map[ch] = letters[(idx + 1) % letters.length];
  return map;
}, {});

const increment = (password, idx = 0) => {
  if (idx === password.length) return password.push(letters[0]);
  password[idx] = nextLetter[password[idx]];
  if (password[idx] === letters[0]) increment(password, idx + 1);
};

const findNext = password => {
  increment(password);

  while (
    [hasIncreasingSequence, hasNoForbiddenLetters, hasTwoPairs].some(
      test => !test(password)
    )
  )
    increment(password);

  return password;
};

exports.solveOne = password => findNext(password).reverse().join('');

exports.solveTwo = password => findNext(findNext(password)).reverse().join('');
