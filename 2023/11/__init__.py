from bisect import bisect_left, bisect_right
from collections import defaultdict

from pyutils import *


def parse(lines):
    return [list(line) for line in lines]


def solve(universe, multiplier):
    def h_distance(universe):
        galaxies = defaultdict(lambda: 0)
        for r in range(len(universe)):
            for c in range(len(universe[0])):
                if universe[r][c] == "#":
                    galaxies[r] += 1
        gaps = [r for r in range(len(universe)) if r not in galaxies]

        distance, rows = 0, list(galaxies.keys())
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                l = bisect_left(gaps, rows[i])
                r = bisect_right(gaps, rows[j])
                distance += (
                    galaxies[rows[i]]
                    * galaxies[rows[j]]
                    * (rows[j] - rows[i] + (r - l) * (multiplier - 1))
                )
        return distance

    transpose = [[] for _ in range(len(universe[0]))]
    for row in universe:
        for c, v in enumerate(row):
            transpose[c].append(v)

    return h_distance(universe) + h_distance(transpose)


@expect({"test": 374})
def solve1(universe):
    return solve(universe, 2)


# @expect({"test": 1030})   # multiplier = 10
# @expect({"test": 8410})   # multiplier = 100
@expect({"test": 82000210})  # multiplier = 1,000,000
def solve2(universe):
    return solve(universe, 1000000)
