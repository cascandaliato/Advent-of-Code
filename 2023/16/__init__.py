from pyutils import *

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
change = {
    ".": {N: [N], S: [S], W: [W], E: [E]},
    "/": {N: [E], S: [W], W: [S], E: [N]},
    "\\": {N: [W], S: [E], W: [N], E: [S]},
    "|": {N: [N], S: [S], W: [N, S], E: [N, S]},
    "-": {N: [W, E], S: [W, E], W: [W], E: [E]},
}


def parse(lines):
    return lines


def solve(grid, start):
    q, visited = [start], set()
    while q:
        beam = q.pop()
        (r, c), dir_ = beam
        if beam in visited or r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            continue
        visited.add(beam)

        for new_dir in change[grid[r][c]][dir_]:
            q.append(((r + new_dir[0], c + new_dir[1]), new_dir))

    return len(set((r, c) for (r, c), _ in visited))


@expect({"test": 46})
def solve1(grid):
    return solve(grid, ((0, 0), (0, 1)))


@expect({"test": 51})
def solve2(grid):
    max_power = 0
    for r in range(len(grid)):
        max_power = max(max_power, solve(grid, ((r, 0), (0, 1))))
        max_power = max(max_power, solve(grid, ((r, len(grid[0]) - 1), (0, -1))))
    for c in range(len(grid[0])):
        max_power = max(max_power, solve(grid, ((0, c), (1, 0))))
        max_power = max(max_power, solve(grid, ((len(grid) - 1, c), (-1, 0))))
    return max_power
