from pyutils import *


def parse(lines):
    instructions = []
    for s in lines[0].split(", "):
        instructions.append((s[0], int(s[1:])))
    return instructions


rotation = {
    "R": [[0, 1], [-1, 0]],
    "L": [[0, -1], [1, 0]],
}


def rotate(direction, r):
    return [
        direction[0] * rotation[r][0][0] + direction[1] * rotation[r][0][1],
        direction[0] * rotation[r][1][0] + direction[1] * rotation[r][1][1],
    ]


@expect({"test1": 5, "test2": 2, "test3": 12})
def solve1(instructions):
    x, y = 0, 0
    facing = [0, 1]  # north
    for r, n in instructions:
        facing = rotate(facing, r)
        x += n * facing[0]
        y += n * facing[1]
    return abs(x) + abs(y)


@expect({"test4": 4})
def solve2(instructions):
    visited = set([(0, 0)])
    x, y = 0, 0
    facing = [0, 1]  # north
    for r, n in instructions:
        facing = rotate(facing, r)
        for _ in range(n):
            x += facing[0]
            y += facing[1]
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))
