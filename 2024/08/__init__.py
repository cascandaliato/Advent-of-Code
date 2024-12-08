from collections import defaultdict
from itertools import combinations, count

from pyutils import *


def parse(lines):
    antennas = defaultdict(set)
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if (pos := lines[r][c]) != ".":
                antennas[pos].add((r, c))
    return antennas, len(lines), len(lines[0])


@expect({"test": 14})
def solve1(input):
    antennas, r, c = input

    def is_valid_location(x, y):
        return 0 <= x < r and 0 <= y < c

    antinodes = set()
    for a in antennas.values():
        for (r1, c1), (r2, c2) in combinations(a, 2):
            dr, dc = r2 - r1, c2 - c1
            if is_valid_location(r2 + dr, c2 + dc):
                antinodes.add((r2 + dr, c2 + dc))
            if is_valid_location(r1 - dr, c1 - dc):
                antinodes.add((r1 - dr, c1 - dc))
    return len(antinodes)


@expect({"test": 34})
def solve2(input):
    antennas, r, c = input

    antinodes = set()

    def propagate(x, y, dx, dy):
        for i in count():
            if not (0 <= x + i * dx < r and 0 <= y + i * dy < c):
                return
            antinodes.add((x + i * dx, y + i * dy))

    for a in antennas.values():
        for (r1, c1), (r2, c2) in combinations(a, 2):
            dr, dc = r2 - r1, c2 - c1
            propagate(r2, c2, dr, dc)
            propagate(r1, c1, -dr, -dc)

    return len(antinodes)
