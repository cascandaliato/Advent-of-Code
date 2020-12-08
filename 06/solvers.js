const { flow, intersection, spread, sum, union } = require('lodash');
const { get, map } = require('lodash/fp');
const { splitByBlankLine } = require('../utils');

exports.normalizeInput = flow(splitByBlankLine, map(map(line => [...line])));

exports.solveOne = flow(map(spread(union)), map(get('length')), sum);

exports.solveTwo = flow(map(spread(intersection)), map(get('length')), sum);
