const fs = require('fs');

const passwords = fs
  .readFileSync('input.txt')
  .toString()
  .split('\r\n')
  .map(line => {
    const [minMax, letterColon, password] = line.split(' ');
    const [min, max] = minMax.split('-').map(Number);
    const [letter] = letterColon[0];
    return { password, letter, min, max };
  });

const countValid = () =>
  passwords.filter(({ password, letter, min, max }) => {
    const counter = new Map();
    [...password].forEach(ch => counter.set(ch, counter.get(ch) + 1 || 1));
    return counter.get(letter) >= min && counter.get(letter) <= max;
  }).length;

console.log('Part One: ', countValid());

const countOfficiallyValid = () =>
  passwords.filter(
    ({ password, letter, min: left, max: right }) =>
      (password[left - 1] === letter && password[right - 1] !== letter) ||
      (password[left - 1] !== letter && password[right - 1] === letter)
  ).length;

console.log('Part Two: ', countOfficiallyValid());
