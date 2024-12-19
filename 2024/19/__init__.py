from functools import cache

from pyutils import *


def parse(lines):
    patterns = tuple(lines[0].split(", "))
    designs = lines[2:]
    return patterns, designs


@expect({"test": 6})
def solve1(input):
    patterns, designs = input

    @cache
    def possible(design):
        if not design:
            return True
        return any(possible(design[len(p) :]) for p in patterns if design.startswith(p))

    return sum(possible(d) for d in designs)


@expect({"test": 16})
def solve2(input):
    patterns, designs = input

    @cache
    def count(design):
        if not design:
            return 1
        return sum(count(design[len(p) :]) for p in patterns if design.startswith(p))

    return sum(count(d) for d in designs)
