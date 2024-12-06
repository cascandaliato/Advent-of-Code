from pyutils import *


def parse(lines):
    guard, obstacles = None, set()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            match lines[r][c]:
                case "^":
                    guard = [r, c]
                case "#":
                    obstacles.add((r, c))
    return guard, obstacles, lines


@expect({"test": 41})
def solve1(input):
    (gr, gc), obstacles, grid = input

    visited = set()
    directions, d = [(-1, 0), (0, 1), (1, 0), (0, -1)], 0
    while 0 <= gr < len(grid) and 0 <= gc < len(grid[0]):
        visited.add((gr, gc))
        while (gr + directions[d][0], gc + directions[d][1]) in obstacles:
            d = (d + 1) % 4
        gr += directions[d][0]
        gc += directions[d][1]
    return len(visited)


@expect({"test": 6})
def solve2(input):
    (gr0, gc0), obstacles, grid = input

    gr, gc = gr0, gc0
    visited = set()
    directions, d = [(-1, 0), (0, 1), (1, 0), (0, -1)], 0
    while 0 <= gr < len(grid) and 0 <= gc < len(grid[0]):
        visited.add((gr, gc))
        while (gr + directions[d][0], gc + directions[d][1]) in obstacles:
            d = (d + 1) % 4
        gr += directions[d][0]
        gc += directions[d][1]
    visited.remove((gr0, gc0))

    res = 0
    for v in visited:
        gr, gc, d, states, obstacles_plus = gr0, gc0, 0, set(), obstacles | {v}
        while 0 <= gr < len(grid) and 0 <= gc < len(grid[0]):
            if (gr, gc, d) in states:
                res += 1
                break
            states.add((gr, gc, d))
            while (gr + directions[d][0], gc + directions[d][1]) in obstacles_plus:
                d = (d + 1) % 4
            gr += directions[d][0]
            gc += directions[d][1]

    return res
