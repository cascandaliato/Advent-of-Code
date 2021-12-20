from pyutils import *


def parse(lines):
    dots, instructions = split_by_empty_line(lines)
    return set(tuple(int(n) for n in dot.split(',')) for dot in dots), [(dir, int(n)) for dir, n in [instr[11:].split('=') for instr in instructions]]


def fold(dots, instruction):
    dir, n = instruction
    if dir == 'x':
        for x, y in list(filter(lambda t: t[0] > n, dots)):
            dots.add((n-(x-n), y))
            dots.remove((x, y))
    elif dir == 'y':
        for x, y in list(filter(lambda t: t[1] > n, dots)):
            dots.add((x, n-(y-n)))
            dots.remove((x, y))


@expect({'test': 17})
def solve1(input):
    dots, instructions = input
    fold(dots, instructions[0])
    return len(dots)


@expect({'test': None})
def solve2(input):
    dots, instructions = input
    for instruction in instructions:
        fold(dots, instruction)
    xmax, ymax = max(x for x, _ in dots), max(y for _, y in dots)
    for y in range(ymax+1):
        print(''.join(['#' if (x, y) in dots else '.' for x in range(xmax+1)]))
    return None
