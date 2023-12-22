from pyutils import *


def parse(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "S":
                return (r, c), grid


def count(data, n):
    (start_r, start_c), grid = data
    q, visited = [(start_r, start_c)], dict()
    for i in range(n + 1):
        new_q = []
        for r, c in q:
            if (r, c) in visited or grid[r % len(grid)][c % len(grid[0])] == "#":
                continue
            visited[(r, c)] = i
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_q.append((r + dr, c + dc))
        q = new_q
    return len([steps for steps in visited.values() if steps % 2 == n % 2])


def solve1(data):
    return count(data, 64)


def solve2(data):
    # https://en.wikipedia.org/wiki/Lagrange_polynomial#Definition
    points = [(i, count(data, 65 + i * 131)) for i in range(3)]
    n = 202300  # (26501365 - 65) // 131
    return int(
        ((n - points[1][0]) * (n - points[2][0]))
        / ((points[0][0] - points[1][0]) * (points[0][0] - points[2][0]))
        * points[0][1]
        + ((n - points[0][0]) * (n - points[2][0]))
        / ((points[1][0] - points[0][0]) * (points[1][0] - points[2][0]))
        * points[1][1]
        + ((n - points[0][0]) * (n - points[1][0]))
        / ((points[2][0] - points[0][0]) * (points[2][0] - points[1][0]))
        * points[2][1]
    )
