from itertools import count

from pyutils import *


def parse(lines):
    east, south = set(), set()
    dimx, dimy = len(lines[0]), len(lines)
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '>':
                east.add((x, y))
            elif char == 'v':
                south.add((x, y))
    return east, south, dimx, dimy


@expect({'test': 58})
def solve1(input):
    east, south, dimx, dimy = input

    for i in count(1):
        new_east, new_south = set(), set()
        for x, y in east:
            candidate = ((x+1) % dimx, y)
            new_east.add(
                (x, y) if candidate in east or candidate in south else candidate)
        for x, y in south:
            candidate = (x, (y+1) % dimy)
            new_south.add(
                (x, y) if candidate in new_east or candidate in south else candidate)
        if new_east == east and new_south == south:
            return i
        east, south = new_east, new_south


def solve2(_):
    pass
