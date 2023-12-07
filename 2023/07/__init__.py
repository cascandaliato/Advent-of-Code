from collections import Counter
from functools import cmp_to_key
from pyutils import *

letters = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def parse(lines):
    hands = []
    for line in lines:
        hand, bid = line.split()
        hands.append(
            (tuple(int(d) if d.isdigit() else letters[d] for d in hand), int(bid))
        )
    return hands


def rank(hand):
    jokers = len([j for j in hand if j == 0])
    if jokers == 5:
        return 7
    freqs = Counter([n for n in hand if n > 0]).most_common()
    first = freqs[0][1] + jokers
    if first >= 4:
        return first + 2
    elif first == 3:
        second = freqs[1][1]
        return first + second
    elif first <= 2:
        second = freqs[1][1]
        return first + second - 1


def compare(a, b):
    ra = rank(a[0])
    rb = rank(b[0])
    if ra != rb:
        return ra - rb
    else:
        for i in range(len(a[0])):
            if a[0][i] != b[0][i]:
                return a[0][i] - b[0][i]
    return 0


@expect({"test": 6440})
def solve1(hands):
    hands.sort(key=cmp_to_key(compare))
    return sum((i + 1) * h[1] for i, h in enumerate(hands))


@expect({"test": 5905})
def solve2(hands):
    return solve1(
        [(tuple(n if n != 11 else 0 for n in hand[0]), hand[1]) for hand in hands]
    )
