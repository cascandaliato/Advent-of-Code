const { intersection } = require('lodash');

exports.normalizeInput = lines =>
  lines.map(line => {
    const [ingredients, allergens] = line.slice(0, -1).split(' (contains ');
    return {
      ingredients: new Set(ingredients.split(' ')),
      allergens: new Set(allergens.split(', ')),
    };
  });

const categorizeIngredientsAndAllergens = menu => {
  const allIngredients = new Set(
    menu.flatMap(({ ingredients }) => [...ingredients])
  );
  const allAllergens = new Set(menu.flatMap(({ allergens }) => [...allergens]));
  const allergenToIngredients = new Map(
    [...allAllergens].map(allergen => [allergen, new Set(allIngredients)])
  );

  for (const allergen of allAllergens) {
    for (const { ingredients, allergens } of menu) {
      if (allergens.has(allergen)) {
        allergenToIngredients.set(
          allergen,
          new Set(
            intersection(
              [...ingredients],
              [...allergenToIngredients.get(allergen)]
            )
          )
        );
      }
    }
  }

  const nonAllergenic = [...allIngredients].filter(ingredient =>
    [...allergenToIngredients].every(
      ([_, potentialAllergenics]) => !potentialAllergenics.has(ingredient)
    )
  );

  return { allergenToIngredients, nonAllergenic };
};

exports.solveOne = menu =>
  categorizeIngredientsAndAllergens(menu)
    .nonAllergenic.map(
      ingredient =>
        menu.filter(({ ingredients }) => ingredients.has(ingredient)).length
    )
    .reduce((a, b) => a + b);

exports.solveTwo = menu => {
  const { allergenToIngredients } = categorizeIngredientsAndAllergens(menu);

  while (
    [...allergenToIngredients].some(([_, ingredients]) => ingredients.size > 1)
  ) {
    for (const [allergen, ingredients] of allergenToIngredients) {
      if (ingredients.size === 1) {
        const allergenic = [...ingredients][0];
        for (const [otherAllergen, otherIngredients] of allergenToIngredients) {
          if (otherAllergen === allergen) continue;
          otherIngredients.delete(allergenic);
        }
      }
    }
  }

  const dangerous = [];
  for (const [, ingredients] of [...allergenToIngredients].sort()) {
    dangerous.push([...ingredients][0]);
  }
  return dangerous.join(',');
};
