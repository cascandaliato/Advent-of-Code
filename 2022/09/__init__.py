from pyutils import *

directions = {"R": (1, 0), "L": (-1, 0), "D": (0, -1), "U": (0, +1)}


def parse(lines):
    instructions = []
    for line in lines:
        direction, steps = line.split()
        instructions.append((direction, int(steps)))
    return instructions


def solve(n, instructions):
    knots, visited = [(0, 0)] * n, set([(0, 0)])

    for direction, steps in instructions:
        dx, dy = directions[direction][0], directions[direction][1]
        for _ in range(steps):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i in range(1, len(knots)):
                if (
                    max(
                        abs(knots[i][0] - knots[i - 1][0]),
                        abs(knots[i][1] - knots[i - 1][1]),
                    )
                    >= 2
                ):
                    knots[i] = (
                        knots[i][0] +
                        max(-1, min(1, knots[i - 1][0] - knots[i][0])),
                        knots[i][1] +
                        max(-1, min(1, knots[i - 1][1] - knots[i][1])),
                    )
            visited.add(knots[-1])

    return len(visited)


@expect({'test1': 13})
def solve1(instructions):
    return solve(2, instructions)


@expect({'test1': 1, 'test2': 36})
def solve2(instructions):
    return solve(10, instructions)
