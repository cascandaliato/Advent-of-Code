from collections import defaultdict
from functools import cache
from itertools import permutations

from pyutils import *


def parse(lines):
    return lines


numeric_keypad = {
    "A": (0, 0),
    "0": (1, 0),
    "1": (2, 1),
    "2": (1, 1),
    "3": (0, 1),
    "4": (2, 2),
    "5": (1, 2),
    "6": (0, 2),
    "7": (2, 3),
    "8": (1, 3),
    "9": (0, 3),
}

directional_keypad = {"A": (0, 0), "<": (2, 1), ">": (0, 1), "^": (1, 0), "v": (1, 1)}


def solve(input, robots):
    routes = defaultdict(set)

    for a, (xa, ya) in numeric_keypad.items():
        for b, (xb, yb) in numeric_keypad.items():
            dx, dy = xb - xa, yb - ya
            dirs = ("<" if dx > 0 else ">") * abs(dx) + ("^" if dy > 0 else "v") * abs(
                dy
            )
            for p in map(lambda p: "".join(p), permutations(dirs)):
                if ya == 0 and xb == 2 and p.startswith("<" * dx):
                    continue
                if xa == 2 and yb == 0 and p.startswith("v" * (-dy)):
                    continue
                routes[(a, b)].add("".join(p) + "A")

    for a, (xa, ya) in directional_keypad.items():
        for b, (xb, yb) in directional_keypad.items():
            dx, dy = xb - xa, yb - ya
            dirs = ("<" if dx > 0 else ">") * abs(dx) + ("v" if dy > 0 else "^") * abs(
                dy
            )
            for p in map(lambda p: "".join(p), permutations(dirs)):
                if ya == 0 and xb == 2 and p.startswith("<" * dx):
                    continue
                if xa == 2 and yb == 0 and p.startswith("^" * (-dy)):
                    continue
                routes[(a, b)].add("".join(p) + "A")

    @cache
    def dp(seq, level=0):
        if level == robots + 1:
            return len(seq)
        length = 0
        for start, end in zip("A" + seq, seq):
            lengths = [dp(r, level + 1) for r in routes[(start, end)]]
            length += min(lengths)
        return length

    res = 0
    for seq in input:
        res += dp(seq) * int(seq[:-1])
    return res


@expect({"test": 126384})
def solve1(input):
    return solve(input, robots=2)


def solve2(input):
    return solve(input, robots=25)
