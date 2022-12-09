from pyutils import *


def parse(lines):
    return lines[0]


def find_marker(chars, n):
    for i in range(n, len(chars)):
        if len(set(chars[i-n:i])) == n:
            return i


@expect({'test': 7})
def solve1(chars):
    return find_marker(chars, 4)


@expect({'test': 19})
def solve2(chars):
    return find_marker(chars, 14)
