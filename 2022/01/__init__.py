from pyutils import *


def parse(lines):
    return [ints(c) for c in split_by_empty_line(lines)]


@expect({'test': 24000})
def solve1(inventories):
    return max(sum(calories) for calories in inventories)


@expect({'test': 45000})
def solve2(inventories):
    return sum(list(sorted((sum(calories) for calories in inventories), reverse=True))[:3])
