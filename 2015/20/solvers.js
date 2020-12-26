exports.normalizeInput = lines => Number(lines[0]);

const solve = (giftMultiplier, maxHousePerElf) => minPresents => {
  const maxHouse = minPresents / 10;
  const houses = new Uint32Array(maxHouse + 1);
  for (let elf = 1; elf <= maxHouse; elf++)
    for (let mult = 1; elf * mult <= maxHouse && mult <= maxHousePerElf; mult++)
      houses[elf * mult] += elf * giftMultiplier;

  for (let i = 1; ; i++) if (houses[i] >= minPresents) return i;
};

exports.solveOne = solve(10, +Infinity);

exports.solveTwo = solve(11, 50);
