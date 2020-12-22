const { splitByBlankLine } = require('../../utils');

exports.normalizeInput = lines =>
  splitByBlankLine(lines).map(decks => decks.slice(1).map(Number).reverse());

const getScore = deck =>
  deck.map((n, idx) => n * (idx + 1)).reduce((a, b) => a + b, 0);

exports.solveOne = ([deck1, deck2]) => {
  while (deck1.length > 0 && deck2.length > 0) {
    const [card1, card2] = [deck1.pop(), deck2.pop()];
    if (card1 > card2) {
      deck1.unshift(card1);
      deck1.unshift(card2);
    } else {
      deck2.unshift(card2);
      deck2.unshift(card1);
    }
  }

  return deck1.length > 0 ? getScore(deck1) : getScore(deck2);
};

const playRecursiveCombat = (deck1, deck2, isSubGame = false) => {
  const memo = new Set();

  while (deck1.length > 0 && deck2.length > 0) {
    const state = getScore(deck1) * getScore(deck2);
    if (memo.has(state)) return 1;
    memo.add(state);

    let turnWinner;
    const [card1, card2] = [deck1.pop(), deck2.pop()];
    if (deck1.length >= card1 && deck2.length >= card2) {
      turnWinner = playRecursiveCombat(
        deck1.slice(-card1),
        deck2.slice(-card2),
        true
      );
    } else {
      turnWinner = card1 > card2 ? 1 : 2;
    }

    if (turnWinner === 1) {
      deck1.unshift(card1);
      deck1.unshift(card2);
    } else {
      deck2.unshift(card2);
      deck2.unshift(card1);
    }
  }

  return deck1.length > 0 ? 1 : 2;
};

exports.solveTwo = ([deck1, deck2]) =>
  playRecursiveCombat(deck1, deck2) === 1 ? getScore(deck1) : getScore(deck2);
