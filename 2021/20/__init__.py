from itertools import product

from pyutils import *


def parse(lines):
    algo, image = split_by_empty_line(lines)
    return ''.join(algo), sparse([list(line) for line in image])


def idx(image, pos):
    (x, y), bits = pos, ''
    for dx, dy in sorted(product([-1, 0, 1], repeat=2), key=lambda t: t[1]):
        bits += str(int((x+dx, y+dy) in image))
    return int(bits, 2)


def transform(image, algo, round):
    if algo[0] == '.':
        augmented = set((x+dx, y+dy) for x, y in image for dx,
                        dy in product([-1, 0, 1], repeat=2))
        return set(pos for pos in augmented if algo[idx(image, pos)] == '#')
    else:
        if round % 2 == 1:
            augmented = set((x+dx, y+dy) for x, y in image for dx,
                            dy in product([-1, 0, 1], repeat=2))
            return set(pos for pos in augmented if algo[idx(image, pos)] == '.')
        else:
            augmented = set((x+dx, y+dy) for x, y in image for dx,
                            dy in product([-1, 0, 1], repeat=2))
            return set(pos for pos in augmented if algo[idx(image, pos) ^ (2**9 - 1)] == '#')


def solve(algo, image, rounds):
    for round in range(rounds):
        image = transform(image, algo, round+1)
    return len(image)


@expect({'test': 35})
def solve1(input):
    return solve(*input, 2)


@expect({'test': 3351})
def solve2(input):
    return solve(*input, 50)
