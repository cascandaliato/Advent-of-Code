from string import ascii_letters
from pyutils import *

priorities = {letter: idx+1 for idx, letter in enumerate(ascii_letters)}


def parse(rucksacks):
    return rucksacks


@expect({'test': 157})
def solve1(rucksacks):
    return sum(priorities[next(iter(set(r[0:len(r)//2]).intersection(set(r[len(r)//2:]))))]
               for r in rucksacks)


@expect({'test': 70})
def solve2(rucksacks):
    groups = [list(map(set, rucksacks[i:i+3]))
              for i in range(0, len(rucksacks), 3)]
    return sum(priorities[next(iter(g[0].intersection(g[1], g[2])))] for g in groups)
