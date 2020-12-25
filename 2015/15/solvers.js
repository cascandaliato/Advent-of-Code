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

const getBestScore = (filterPredicate = () => true) => byIngredient => {
  const ingredients = keys(byIngredient);
  return (
    // for each partition of 100
    [...numberPartitions(100, ingredients.length)]
      // calculate the total score
      .map(partition =>
        ['capacity', 'durability', 'flavor', 'texture', 'calories']
          .map(property =>
            partition
              .map(
                (quantity, idx) =>
                  byIngredient[ingredients[idx]][property] * quantity
              )
              .reduce((a, b) => a + b)
          )
          .map((score, _, properties) =>
            filterPredicate(properties) ? Math.max(score, 0) : 0
          )
          // (discard calories)
          .slice(0, -1)
          .reduce((a, b) => a * b)
      )
      // and return the max
      .reduce((a, b) => Math.max(a, b))
  );
};

exports.solveOne = getBestScore();

exports.solveTwo = getBestScore(([, , , , calories]) => calories === 500);
