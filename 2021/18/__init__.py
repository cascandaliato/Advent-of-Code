from itertools import product
from math import ceil, floor, inf

from pyutils import *


def parse(lines):
    return [transform(line) for line in lines]


def transform(snail):
    number, depth = [], 0
    for char in snail:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char == ',':
            continue
        else:
            number.append([int(char), depth])
    return number


def add(n1, n2):
    return [[n, l+1] for n, l in n1+n2]


def reduce(n):
    while explode(n) or split(n):
        continue
    return n


def explode(n):
    idx = findindex(lambda i, _: n[i][1] == n[i+1][1] and n[i][1] > 4, n[:-1])
    if idx == -1:
        return False
    if idx > 0:
        n[idx-1][0] += n[idx][0]
    if idx < len(n)-2:
        n[idx+2][0] += n[idx+1][0]
    n[idx:idx+2] = [[0, 4]]
    return True


def split(n):
    idx = findindex(lambda _, ni: ni[0] >= 10, n)
    if idx == -1:
        return False
    n[idx:idx+1] = [[floor(n[idx][0]/2), n[idx][1]+1],
                    [ceil(n[idx][0]/2), n[idx][1]+1]]
    return True


def magnitude(n):
    while len(n) > 1:
        idx = findindex(lambda i, _: n[i][1] == n[i+1][1], n[:-1])
        mag = 3*n[idx][0] + 2*n[idx+1][0]
        n = n[:idx] + [[mag, n[idx][1]-1]] + n[idx+2:]
    return n[0][0]


@expect({'test1': 445, 'test2': 791, 'test3': 1137, 'test4': 3488, 'test5': 4140})
def solve1(input):
    total = input[0]
    for n in input[1:]:
        total = reduce(add(total, n))
    return magnitude(total)


@expect({'test5': 3993})
def solve2(input):
    max_magnitude = -inf
    for n1, n2 in filter(lambda p: p[0] != p[1], product(input, repeat=2)):
        max_magnitude = max(max_magnitude, magnitude(
            reduce(add(n1, n2))))
    return max_magnitude
