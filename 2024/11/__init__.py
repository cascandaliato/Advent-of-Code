from functools import cache

from pyutils import *


def parse(lines):
    return [int(n) for n in lines[0].split()]


@cache
def count(stone, iters):
    res = 1
    for i in reversed(range(iters)):
        if stone == 0:
            stone = 1
        elif len(s := str(stone)) % 2 == 0:
            stone = int(s[: len(s) // 2])
            res += count(int(s[len(s) // 2 :]), i)
        else:
            stone *= 2024
    return res


@expect({"test": 55312})
def solve1(input, iters=25):
    return sum(count(n, iters) for n in input)


def solve2(input):
    return solve1(input, 75)
