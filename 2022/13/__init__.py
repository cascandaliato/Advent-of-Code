import functools

from json import loads

from pyutils import *


def parse(lines):
    return [[loads(g[0]), loads(g[1])] for g in split_by_empty_line(lines)]


def compare(left, right):
    if type(left) is list and type(right) is int:
        return compare(left, [right])

    if type(left) is int and type(right) is list:
        return compare([left], right)

    if type(left) is int and type(right) is int:
        return -1 if left < right else 0 if left == right else 1

    if type(left) is list and type(right) is list:
        i = 0
        while True:
            if len(left) <= i < len(right):
                return -1
            if len(right) <= i < len(left):
                return 1
            if i >= len(left) and i >= len(right):
                return 0
            c = compare(left[i], right[i])
            if c == 0:
                i += 1
            else:
                return c


@expect({'test': 13})
def solve1(groups):
    return sum(i+1 for i, g in enumerate(groups) if compare(g[0], g[1]) == -1)


@expect({'test': 140})
def solve2(groups):
    packets = [n for g in groups for n in g] + [[[2]], [[6]]]
    indexes = [i+1 for i, g in enumerate(
        sorted(packets, key=functools.cmp_to_key(compare))) if g in ([[2]], [[6]])]
    return indexes[0]*indexes[1]
