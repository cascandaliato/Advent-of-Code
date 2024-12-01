from collections import Counter

from pyutils import *


def parse(lines):
    l1, l2 = [], []
    for line in lines:
        n1, n2 = line.split()
        l1.append(int(n1))
        l2.append(int(n2))
    return l1, l2


@expect({"test": 11})
def solve1(input):
    l1, l2 = input
    return sum(abs(n2 - n1) for n1, n2 in zip(sorted(l1), sorted(l2)))


@expect({"test": 31})
def solve2(input):
    l1, c2 = input[0], Counter(input[1])
    return sum(n1 * c2[n1] for n1 in l1)
