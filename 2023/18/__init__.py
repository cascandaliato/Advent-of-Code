from collections import defaultdict
from pyutils import *


def parse(lines):
    data = []
    for line in lines:
        dir_, n, color = line.split(" ")
        data.append((dir_, int(n), color[1:-1]))
    return data


@expect({"test": 62})
def solve1(data):
    dirs = {
        "R": (0, 1),
        "L": (0, -1),
        "D": (1, 0),
        "U": (-1, 0),
    }

    trench, border = [], 0
    r, c = 0, 0
    for dir_, n, _ in data:
        dr, dc = dirs[dir_]
        r += dr * n
        c += dc * n
        trench.append((r, c))
        border += n

    # https://en.wikipedia.org/wiki/Shoelace_formula#Trapezoid_formula
    trench.append(trench[0])
    area = 0
    for i in range(len(trench) - 1):
        area += (trench[i][1] + trench[i + 1][1]) * (trench[i][0] - trench[i + 1][0])
    area //= 2

    # https://en.wikipedia.org/wiki/Pick%27s_theorem
    return border + abs(area) - border // 2 + 1


@expect({"test": 952408144115})
def solve2(data):
    dirs = ["R", "D", "L", "U"]
    for i, (_, _, rgb) in enumerate(data):
        data[i] = (dirs[int(rgb[-1])], int(rgb[1:-1], base=16), None)
    return solve1(data)
