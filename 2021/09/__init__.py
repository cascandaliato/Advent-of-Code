from math import inf

from pyutils import *


def parse(lines):
    heights = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            heights[(x, y)] = int(char)
    return heights


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def lows(heights):
    return [(x, y) for (x, y), h in heights.items() if all(h < heights[(x+dx, y+dy)] for dx, dy in directions if (x+dx, y+dy) in heights)]


@expect({'test': 15})
def solve1(heights):
    return sum(1+heights[(x, y)] for x, y in lows(heights))


def basin_from(x, y, heights):
    q, basin = [(x, y, -inf)], set()
    while q:
        x, y, prev = q.pop()
        if (x, y) not in heights or (x, y) in basin or heights[(x, y)] == 9:
            continue
        if heights[(x, y)] > prev:
            basin.add((x, y))
            q.extend([(x+dx, y+dy, heights[(x, y)])
                      for dx, dy in directions])
    return tuple(sorted(basin))


@expect({'test': 1134})
def solve2(heights):
    answer = 1
    for basin in sorted(set(basin_from(x, y, heights) for x, y in lows(heights)), key=len, reverse=True)[:3]:
        answer *= len(basin)
    return answer
