from math import inf

from pyutils import *


def parse(lines):
    heights = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            heights[(x, y)] = int(char)
    return heights


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def neighbors(loc, heights):
    for direction in directions:
        neighbor = tuple(x+dx for x, dx in zip(loc, direction))
        if neighbor in heights:
            yield neighbor


def lows(heights):
    return [loc for loc, height in heights.items() if all(height < heights[neighbor] for neighbor in neighbors(loc, heights))]


def basin_from(low, heights):
    q, basin = [(low, -inf)], set()
    while q:
        loc, prev = q.pop()
        if loc in basin or heights[loc] == 9:
            continue
        if heights[loc] > prev:
            basin.add(loc)
            q.extend([(neighbor, heights[loc])
                     for neighbor in neighbors(loc, heights)])
            heights[loc] = 9
    return tuple(sorted(basin))


@expect({'test': 15})
def solve1(heights):
    return sum(1+heights[loc] for loc in lows(heights))


@expect({'test': 1134})
def solve2(heights):
    answer = 1
    for basin in sorted([basin_from(low, heights) for low in lows(heights)], key=len, reverse=True)[:3]:
        answer *= len(basin)
    return answer
