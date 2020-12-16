const { splitByBlankLine } = require('../../utils');

exports.normalizeInput = lines => {
  const [rules, ownTicket, nearbyTickets] = splitByBlankLine(lines);
  return {
    rules: rules.map(rule => {
      const [field, ranges] = rule.split(': ');
      return {
        field,
        ranges: ranges.split(' or ').map(range => range.split('-').map(Number)),
      };
    }),
    ownTicket: ownTicket[1].split(',').map(Number),
    nearbyTickets: nearbyTickets
      .slice(1)
      .map(ticket => ticket.split(',').map(Number)),
  };
};

exports.solveOne = ({ rules, nearbyTickets }) =>
  nearbyTickets
    .flatMap(ticket =>
      ticket.filter(value =>
        rules.every(({ ranges }) =>
          ranges.every(([l, r]) => value < l || value > r)
        )
      )
    )
    .reduce((a, b) => a + b);

exports.solveTwo = ({ rules, ownTicket, nearbyTickets }) => {
  const validTickets = nearbyTickets.filter(ticket =>
    ticket.every(value =>
      rules.some(({ ranges }) =>
        ranges.some(([l, r]) => value >= l && value <= r)
      )
    )
  );

  const fields = Array.from({ length: rules.length }, () => []);

  for (let i = 0; i < fields.length; i++) {
    for (const { field, ranges } of rules) {
      if (
        validTickets.every(ticket =>
          ranges.some(([l, r]) => ticket[i] >= l && ticket[i] <= r)
        )
      ) {
        fields[i].push(field);
      }
    }
  }

  while (fields.some(candidates => candidates.length > 1)) {
    for (let i = 0; i < rules.length; i++) {
      if (fields[i].length === 1) {
        for (let j = 0; j < rules.length; j++) {
          if (j === i) continue;
          fields[j] = fields[j].filter(f => f !== fields[i][0]);
        }
      }
    }
  }

  return fields
    .flat()
    .map((f, idx) => [f, idx])
    .filter(([f]) => /^departure/.test(f))
    .map(([_, idx]) => ownTicket[idx])
    .reduce((a, b) => a * b);
};
