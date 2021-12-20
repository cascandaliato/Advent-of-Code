from heapq import heappop, heappush

from pyutils import *


def parse(lines):
    return [ints(line) for line in lines]


def neighbors(r, c, d):
    return [pos for pos in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if 0 <= pos[0] < d and 0 <= pos[1] < d]


def dijkstra(grid):
    visited, q = set(), [(0, (0, 0))]
    while q:
        risk, pos = heappop(q)
        if pos == (len(grid)-1, len(grid)-1):
            return risk
        if pos in visited:
            continue
        visited.add(pos)
        for neighbor in neighbors(*pos, len(grid)):
            heappush(q, (risk + grid[neighbor[0]][neighbor[1]], neighbor))


def enlarged(grid):
    return [[(grid[r % len(grid)][c % len(
        grid)] + r//len(grid) + c//len(grid) - 1) % 9 + 1 for c in range(len(grid)*5)] for r in range(len(grid)*5)]


@expect({'test': 40})
def solve1(grid):
    return dijkstra(grid)


@expect({'test': 315})
def solve2(grid):
    return dijkstra(enlarged(grid))
