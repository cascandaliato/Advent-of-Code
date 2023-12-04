from pyutils import *


def parse(lines):
    def ints(s):
        return [int(n) for n in s.split()]

    cards = []
    for i, line in enumerate(lines):
        win, have = line.split(": ")[1].split(" | ")
        win, have = ints(win), ints(have)
        matches = 0
        for n in win:
            if n in have:
                matches += 1
        cards.append(matches)
    return cards


@expect({"test": 13})
def solve1(cards):
    return sum(int(2 ** (matches - 1)) for matches in cards)


@expect({"test": 30})
def solve2(cards):
    num_cards = [1] * len(cards)
    for i in range(len(cards) - 1):
        for j in range(i + 1, i + 1 + cards[i]):
            num_cards[j] += num_cards[i]
    return sum(num_cards)
