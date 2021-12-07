from pyutils import *


def parse(lines):
    return ints(lines[0].split(','))


def min_cost(positions, cost_unit):
    l, r = min(positions), max(positions)
    return min(sum(cost_unit(t, p) for p in positions) for t in range(l, r+1))


@expect({'test': 37})
def solve1(positions):
    return min_cost(positions, lambda x, y: abs(x-y))


@expect({'test': 168})
def solve2(positions):
    return min_cost(positions, lambda x, y: abs(x-y)*(abs(x-y)+1)//2)
