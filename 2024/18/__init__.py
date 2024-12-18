from collections import deque

from pyutils import *


def parse(lines):
    return [tuple(map(int, line.split(","))) for line in lines]


# @expect({"test": 22})
def solve1(input, size=70, first_steps=1024):
    input = set(input[:first_steps])

    q, visited = deque([(0, 0, 0)]), set()
    while q:
        x, y, steps = q.pop()
        if (x, y) == (size, size):
            return steps
        if (x, y) in visited or (x, y) in input:
            continue
        visited.add((x, y))
        for dx, dy in ((-1, 0), (+1, 0), (0, +1), (0, -1)):
            if 0 <= x + dx <= size and 0 <= y + dy <= size:
                q.appendleft((x + dx, y + dy, steps + 1))


# @expect({"test": "6,1"})
def solve2(input, size=70):
    l, r = 0, len(input) - 1
    while l < r:
        m = (l + r) >> 1
        if solve1(input, size, first_steps=(m + 1)):
            l = m + 1
        else:
            r = m
    return ",".join(map(str, input[m]))
