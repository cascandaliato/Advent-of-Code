from itertools import product

from pyutils import *


def parse(lines):
    return [ints(line) for line in lines]


def neighbors(r, c, d):
    return ((r+dr, c+dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (dc != 0 or dr != 0) and 0 <= r+dr < d and 0 <= c+dc < d)


def update_and_store(grid, r, c, store):
    grid[r][c] = (grid[r][c]+1) % 10
    if grid[r][c] == 0:
        store.add((r, c))


def play(grid):
    count = 0
    lit = set()

    # first pass
    for r, c in product(range(len(grid)), repeat=2):
        update_and_store(grid, r, c, lit)

    # keep looping until no octopus flashes
    while lit:
        count += len(lit)
        newly_lit = set()
        for r, c in lit:
            for nr, nc in neighbors(r, c, len(grid)):
                if grid[nr][nc]:
                    update_and_store(grid, nr, nc, newly_lit)
        lit = newly_lit
    return count


@expect({'test': 1656})
def solve1(grid):
    return sum(play(grid) for _ in range(100))


@expect({'test': 195})
def solve2(grid):
    i = 1
    while play(grid) != len(grid)**2:
        i += 1
    return i
