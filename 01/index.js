const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split('\r\n');

const numbers = new Set(input.map(Number));

function findTwo(targetSum) {
  for (const n of numbers) {
    if (numbers.has(targetSum - n)) {
      return n * (targetSum - n);
    }
  }
}

console.log('Part One:', findTwo(2020));

function findThree(targetSum) {
  for (const n of numbers) {
    if (findTwo(targetSum - n)) {
      return n * findTwo(targetSum - n);
    }
  }
}

console.log('Part Two:', findThree(2020));
