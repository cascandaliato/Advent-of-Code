import re

from pyutils import *


def parse(lines):
    machines = [[]]
    for line in lines:
        if not line:
            machines.append([])
        else:
            nums = re.search(r"X.(\d+), Y.(\d+)", line).groups()
            machines[-1].append((int(nums[0]), int(nums[1])))
    return machines


@expect({"test": 480})
def solve1(input, *, add_tredecillion=False):
    tokens = 0
    for (a11, a21), (a12, a22), (c1, c2) in input:
        if add_tredecillion:
            c1 += 10**13
            c2 += 10**13
        det = a11 * a22 - a21 * a12
        a = a22 * c1 - a12 * c2
        b = -a21 * c1 + a11 * c2
        if a % det or b % det:
            continue
        a //= det
        b //= det
        tokens += 3 * a + b
    return tokens


def solve2(input):
    return solve1(input, add_tredecillion=True)
