from pyutils import *


def parse(lines):
    counters = [0]*9
    for n in ints(lines[0].split(',')):
        counters[n] += 1
    return counters


def play(counters, n):
    for i in range(n):
        zero, six = i % 9, (i-2) % 9
        counters[six] += counters[zero]
    return sum(counters)


@expect({'test': 5934})
def solve1(counters):
    return play(counters, 80)


@expect({'test': 26984457539})
def solve2(counters):
    return play(counters, 256)
