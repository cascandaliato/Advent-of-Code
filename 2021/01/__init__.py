from pyutils import *


def parse(lines):
    return list(ints(lines))


@expect({'test': 7})
def solve1(input, d=1):
    return sum(int(a > b) for a, b in zip(input[d:], input[:-d]))


@expect({'test': 5})
def solve2(input):
    return solve1(input, 3)
