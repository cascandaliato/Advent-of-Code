from heapq import heappush, heappop
from pyutils import *


def parse(lines):
    return lines


dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))


def solve(grid, min_, max_):
    # heat_loss, straight_moves, row, column, direction_row, direction_col
    q = [(0, 0, 0, 0, 0, 1)]
    visited = set()
    while q:
        heat_loss, straight_moves, r, c, dr, dc = heappop(q)
        if (
            r < 0
            or r >= len(grid)
            or c < 0
            or c >= len(grid[0])
            or (straight_moves, r, c, dr, dc) in visited
        ):
            continue
        visited.add((straight_moves, r, c, dr, dc))
        heat_loss += int(grid[r][c])
        if r == len(grid) - 1 and c == len(grid[0]) - 1 and straight_moves >= min_:
            return heat_loss - int(grid[0][0])
        for new_dr, new_dc in dirs:
            if (new_dr, new_dc) != (-dr, -dc):
                if (new_dr, new_dc) == (dr, dc):
                    if straight_moves < max_:
                        heappush(
                            q,
                            (
                                heat_loss,
                                straight_moves + 1,
                                r + new_dr,
                                c + new_dc,
                                new_dr,
                                new_dc,
                            ),
                        )
                elif straight_moves >= min_:
                    heappush(q, (heat_loss, 1, r + new_dr, c + new_dc, new_dr, new_dc))
    return None


@expect({"test1": 102})
def solve1(grid):
    return solve(grid, min_=0, max_=3)


@expect({"test1": 94, "test2": 71})
def solve2(grid):
    return solve(grid, min_=4, max_=10)
