from pyutils import *


values = {
    'A': 0, 'B': 1, 'C': 2,
    'X': 0, 'Y': 1, 'Z': 2
}


def parse(lines):
    return [tuple(values[letter] for letter in line.split()) for line in lines]


@expect({'test': 15})
def solve1(rounds):
    return sum(r[1]+1 + ((r[1]-r[0]+1) % 3-1)*3+3 for r in rounds)


@expect({'test': 12})
def solve2(strategy):
    return solve1([(s[0], (s[0]+s[1]-1) % 3) for s in strategy])
