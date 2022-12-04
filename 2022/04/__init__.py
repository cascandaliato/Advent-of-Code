from pyutils import *


def parse(lines):
    ranges = []
    for line in lines:
        r1, r2 = line.split(',')
        s1, e1 = ints(r1.split('-'))
        s2, e2 = ints(r2.split('-'))
        ranges.append(((s1, e1), (s2, e2)))
    return ranges


def includes(r1, r2):
    return r1[0] <= r2[0] <= r2[1] <= r1[1]


def overlaps(r1, r2):
    return r2[0] <= r1[1] <= r2[1] or r1[0] <= r2[1] <= r1[1]


@expect({'test': 2})
def solve1(ranges):
    return len(list(r1 for r1, r2 in ranges if includes(r1, r2) or includes(r2, r1)))


@expect({'test': 4})
def solve2(ranges):
    return len(list(r1 for r1, r2 in ranges if overlaps(r1, r2)))
