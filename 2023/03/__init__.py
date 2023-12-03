from pyutils import *


def parse(lines):
    return lines


def numbers(lines):
    nums = []
    r = 0
    while r < len(lines):
        c = 0
        while c < len(lines[r]):
            if lines[r][c].isdigit():
                i, j = c, c
                while j + 1 < len(lines[r]) and lines[r][j + 1].isdigit():
                    j += 1
                c = j
                nums.append((r, i, j, int(lines[r][i : j + 1])))
            c += 1
        r += 1
    return nums


def symbols(lines, r, i, j):
    for nr, nc in (
        [(r, i - 1), (r, j + 1)]
        + [(r - 1, k) for k in range(i - 1, j + 2)]
        + [(r + 1, k) for k in range(i - 1, j + 2)]
    ):
        if (
            0 <= nr < len(lines)
            and 0 <= nc < len(lines[r])
            and not lines[nr][nc].isdigit()
            and lines[nr][nc] != "."
        ):
            yield (nr, nc, lines[nr][nc])


@expect({"test": 4361})
def solve1(lines):
    return sum(
        n for r, i, j, n in numbers(lines) if next(symbols(lines, r, i, j), None)
    )


@expect({"test": 467835})
def solve2(lines):
    by_symbol = {}
    for r, i, j, n in numbers(lines):
        for symbol in symbols(lines, r, i, j):
            by_symbol.setdefault(symbol, []).append(n)
    return sum(
        adj_nums[0] * adj_nums[1]
        for symbol, adj_nums in by_symbol.items()
        if symbol[2] == "*" and len(adj_nums) == 2
    )
