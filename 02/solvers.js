exports.normalizeInput = lines =>
  lines.map(line => {
    const [minMax, letterColon, password] = line.split(' ');
    const [min, max] = minMax.split('-').map(Number);
    const [letter] = letterColon[0];
    return { password, letter, min, max };
  });

exports.solveOne = passwords =>
  passwords.filter(({ password, letter, min, max }) => {
    const counter = new Map();
    [...password].forEach(ch => counter.set(ch, counter.get(ch) + 1 || 1));
    return counter.get(letter) >= min && counter.get(letter) <= max;
  }).length;

exports.solveTwo = passwords =>
  passwords.filter(
    ({ password, letter, min: left, max: right }) =>
      (password[left - 1] === letter) !== (password[right - 1] === letter)
  ).length;
