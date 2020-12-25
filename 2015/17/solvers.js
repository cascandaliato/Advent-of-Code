exports.normalizeInput = lines => lines.map(Number);

const getCombos = (liters, containers) =>
  Array.from({ length: 2 ** containers.length }, (_, idx) => idx)
    .map(combo => containers.map((_, idx) => (combo >> idx) & 1))
    .filter(
      combo =>
        combo
          .map((bit, idx) => bit * containers[idx])
          .reduce((a, b) => a + b) === liters
    );

exports.getCombos = getCombos;

exports.solveOne = containers => getCombos(150, containers).length;

const getCombosMinContainers = (liters, containers) => {
  const combos = getCombos(liters, containers).map(combo =>
    combo.reduce((a, b) => a + b)
  );
  const minContainers = combos.reduce((a, b) => Math.min(a, b));
  return combos.filter(numContainers => numContainers === minContainers);
};

exports.getCombosMinContainers = getCombosMinContainers;

exports.solveTwo = containers => getCombosMinContainers(150, containers).length;
