const { flow } = require('lodash');
const { tests } = require('../../utils');
const { normalizeInput, solveOne, solveTwo } = require('./solvers');

tests('Part One', flow(normalizeInput, solveOne), [
  {
    input: ['ugknbfddgicrmopn'],
    expectedOutput: 1,
  },
  {
    input: ['aaa'],
    expectedOutput: 1,
  },
  {
    input: ['jchzalrnumimnmhp'],
    expectedOutput: 0,
  },
  {
    input: ['haegwjzuvuyypxyu'],
    expectedOutput: 0,
  },
  {
    input: ['dvszwmarrgswjxmb'],
    expectedOutput: 0,
  },
]);

tests('Part Two', flow(normalizeInput, solveTwo), [
  {
    input: ['qjhvhtzxzqqjkmpb'],
    expectedOutput: 1,
  },
  {
    input: ['xxyxx'],
    expectedOutput: 1,
  },
  {
    input: ['uurcxstgmygtbstg'],
    expectedOutput: 0,
  },
  {
    input: ['ieodomkazucvgmuy'],
    expectedOutput: 0,
  },
]);
