from collections import defaultdict

from pyutils import *


def parse(lines):  # [ ((x1, y1), (x2, y2)), ... ]
    return [tuple(tuple(int(n) for n in coords.split(','))
                  for coords in line.split(' -> ')) for line in lines]


def step(n1, n2):
    return 0 if n1 == n2 else int(n2 >= n1)*2-1


def line(x1, y1, x2, y2):
    x, y, dx, dy = x1, y1, step(x1, x2), step(y1, y2)

    l = set([(x1, y1)])
    while True:
        x, y = x+dx, y+dy
        l.add((x, y))
        if x == x2 and y == y2:
            break
    return l


def count(input):
    field = defaultdict(lambda: 0)

    for (x1, y1), (x2, y2) in input:
        for x, y in line(x1, y1, x2, y2):
            field[(x, y)] += 1

    return len([counter for counter in field.values() if counter >= 2])


@expect({'test': 5})
def solve1(input):
    return count([((x1, y1), (x2, y2))
                  for (x1, y1), (x2, y2) in input if x1 == x2 or y1 == y2])


@expect({'test': 12})
def solve2(input):
    return count(input)
