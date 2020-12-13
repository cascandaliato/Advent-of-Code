const { unzip } = require('lodash');
const { chineseRemainder, mod } = require('../../utils');

exports.normalizeInput = lines => ({
  timestamp: Number(lines[0]),
  buses: lines[1]
    .split(',')
    .map((id, pos) => [id, pos])
    .filter(([id]) => id !== 'x')
    .map(([id, pos]) => [Number(id), pos]),
});

exports.solveOne = ({ timestamp, buses }) =>
  buses
    .map(([id]) => [(id - (timestamp % id)) % id, id])
    .sort(([w1], [w2]) => w1 - w2)[0]
    .reduce((a, b) => a * b);

exports.solveTwo = ({ buses }) =>
  chineseRemainder(...unzip(buses.map(([id, r]) => [id, mod(id - r, id)])));
