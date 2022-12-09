from pyutils import *


def parse(lines):
    return list(map(ints, lines))


@expect({'test': 21})
def solve1(grid):
    def get_visibles(heights):
        visibles = set()
        max_height = -1
        for i in range(len(heights)):
            if heights[i] > max_height:
                visibles.add(i)
                max_height = heights[i]
        return visibles

    visibles = []
    for i in range(len(grid)):
        visibles.extend((i, idx) for idx in get_visibles(grid[i]))
        visibles.extend((i, len(grid) - 1 - idx)
                        for idx in get_visibles(grid[i][::-1]))
        visibles.extend(
            (idx, i) for idx in get_visibles([grid[j][i] for j in range(len(grid))])
        )
        visibles.extend(
            (len(grid) - 1 - idx, i)
            for idx in get_visibles([grid[len(grid) - 1 - j][i] for j in range(len(grid))])
        )
    return len(set(visibles))


@expect({'test': 8})
def solve2(grid):
    def count_visibles(height, heights):
        visibles = 0
        for h in heights:
            visibles += 1
            if h >= height:
                break
        return visibles

    scores = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            h = grid[i][j]
            scores.add(count_visibles(h, list(reversed(grid[i][:j])))
                       * count_visibles(h, grid[i][j + 1:])
                       * count_visibles(h, [grid[idx][j] for idx in range(i - 1, -1, -1)])
                       * count_visibles(h, [grid[idx][j] for idx in range(i + 1, len(grid))]))
    return max(scores)
