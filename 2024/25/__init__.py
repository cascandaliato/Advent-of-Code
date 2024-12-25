from pyutils import *


def parse(lines):
    locks, keys = [], []

    i = 0
    while i < len(lines):
        if not lines[i]:
            i += 1
            continue

        if lines[i][0] == "#":
            locks.append([6] * 5)
            for c in range(5):
                for r in range(1, 7):
                    if lines[i + r][c] == ".":
                        locks[-1][c] = r - 1
                        break
        else:
            keys.append([6] * 5)
            for c in range(5):
                for r in reversed(range(6)):
                    if lines[i + r][c] == ".":
                        keys[-1][c] = 5 - r
                        break

        i += 7

    return locks, keys


@expect({"test": 3})
def solve1(input):
    locks, keys = input

    res = 0
    for lock in locks:
        for key in keys:
            if all(key[i] + lock[i] <= 5 for i in range(5)):
                res += 1
    return res
