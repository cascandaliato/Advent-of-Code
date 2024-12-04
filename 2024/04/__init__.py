import itertools

from pyutils import *


def parse(lines):
    return [[c for c in line] for line in lines]


@expect({"test": 18})
def solve1(input):
    directions = set(itertools.product([-1, 0, 1], repeat=2))
    directions.remove((0, 0))
    target = ["X", "M", "A", "S"]

    res = 0
    for r in range(len(input)):
        for c in range(len(input[0])):
            for dr, dc in directions:
                i = 0
                while (
                    i < len(target)
                    and 0 <= r + i * dr < len(input)
                    and 0 <= c + i * dc < len(input[0])
                    and input[r + i * dr][c + i * dc] == target[i]
                ):
                    i += 1
                if i == len(target):
                    res += 1
    return res


@expect({"test": 9})
def solve2(input):
    res = 0
    for r in range(1, len(input) - 1):
        for c in range(1, len(input[0]) - 1):
            if input[r][c] == "A" and set(
                [input[r - 1][c - 1], input[r + 1][c + 1]]
            ) == set([input[r + 1][c - 1], input[r - 1][c + 1]]) == {"M", "S"}:
                res += 1
    return res
