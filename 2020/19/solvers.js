const { memoize, splitByBlankLine } = require('../../utils');

exports.normalizeInput = lines => {
  const [rules, words] = splitByBlankLine(lines);

  return {
    rules: rules.reduce((rulesMap, rule) => {
      const [name, definition] = rule.split(': ');
      rulesMap[name] = /".*"/.test(definition)
        ? definition.slice(1, -1)
        : definition;
      return rulesMap;
    }, {}),
    words,
  };
};

const resolveRule = memoize((ruleName, rules) => {
  const definition = rules[ruleName];
  if (/^[ab]$/.test(definition)) {
    return definition;
  }
  const resolvedDefinition = definition
    .split(' ')
    .map(token => {
      if (token === '|') {
        return token;
      } else {
        return resolveRule(token, rules);
      }
    })
    .join(' ');
  return `(?:${resolvedDefinition})`.replace(/\s/g, '');
});

const withRuleOverrides = (overrides = {}) => ({ rules, words }) => {
  for (const ruleName in overrides) {
    rules[ruleName] = overrides[ruleName];
  }
  const regex = new RegExp(`^${resolveRule(0, rules)}$`);
  return words.filter(word => regex.test(word)).length;
};

exports.solveOne = withRuleOverrides({});

exports.solveTwo = withRuleOverrides({
  8: '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42',
  11: '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31',
});
