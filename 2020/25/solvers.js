exports.normalizeInput = lines => lines.map(Number);

exports.solveOne = ([pubKeyA, pubKeyB]) => {
  let loopSizeA = 0;

  for (let value = 1; value !== pubKeyA; loopSizeA++)
    value = (value * 7) % 20201227;

  let encryptionKey = 1;
  for (let i = 0; i < loopSizeA; i++)
    encryptionKey = (pubKeyB * encryptionKey) % 20201227;
  return encryptionKey;
};

exports.solveTwo = () => null; // no part two
