from pyutils import *


def parse(lines):
    return [[int(n) for n in line.split()] for line in lines]


@expect({"test": 0})
def solve1(triplets):
    triangles = 0
    for a, b, c in triplets:
        if a + b > c and b + c > a and a + c > b:
            triangles += 1
    return triangles


def solve2(triplets):
    return solve1(
        [
            [triplets[r][c], triplets[r + 1][c], triplets[r + 2][c]]
            for r in range(0, len(triplets), 3)
            for c in range(3)
        ]
    )
