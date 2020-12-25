const { fromPairs, keys } = require('lodash');
const { numberPartitions } = require('../../utils');

exports.normalizeInput = lines =>
  fromPairs(
    lines.map(line => {
      const [ingredient, properties] = line.split(': ');
      return [
        ingredient,
        fromPairs(
          properties.split(', ').map(p => {
            const [property, amount] = p.split(' ');
            return [property, Number(amount)];
          })
        ),
      ];
    })
  );

exports.solveOne = byIngredient => {
  const ingredients = keys(byIngredient);
  return [...numberPartitions(100, ingredients.length)]
    .map(partition => {
      const properties = [
        'capacity',
        'durability',
        'flavor',
        'texture',
      ].map(p =>
        partition
          .map((q, idx) => byIngredient[ingredients[idx]][p] * q)
          .reduce((a, b) => a + b)
      );
      if (properties.some(s => s <= 0)) return 0;
      else return properties.reduce((a, b) => a * b);
    })
    .reduce((a, b) => Math.max(a, b));
};

exports.solveTwo = byIngredient => {
  const ingredients = keys(byIngredient);
  return [...numberPartitions(100, ingredients.length)]
    .map(partition => {
      const properties = [
        'capacity',
        'durability',
        'flavor',
        'texture',
        'calories',
      ].map(p =>
        partition
          .map((q, idx) => byIngredient[ingredients[idx]][p] * q)
          .reduce((a, b) => a + b)
      );
      if (properties.slice(0, -1).some(s => s <= 0) || properties[4] !== 500)
        return 0;
      else return properties.slice(0, -1).reduce((a, b) => a * b);
    })
    .reduce((a, b) => Math.max(a, b));
};
