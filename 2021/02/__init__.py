from functools import reduce
from pyutils import *


def parse(lines):
    return tokens(lines, map=lambda t: (t[0], int(t[1])))


instructions = {
    'forward': lambda pos, dep, aim, n: (pos+n, dep+aim*n, aim),
    'down': lambda pos, dep, aim, n: (pos, dep, aim+n),
    'up': lambda pos, dep, aim, n: (pos, dep, aim-n)
}


def template(input):
    # pos, dep, aim = 0, 0, 0
    # for instruction, n in input:
    #     pos, dep, aim = instructions[instruction](pos, dep, aim, n)
    # return (pos, dep, aim)
    return reduce(lambda t, instr: instructions[instr[0]](*t, instr[1]), input, (0, 0, 0))


@expect({'test': 150})
def solve1(input):
    pos, _, aim = template(input)
    return pos*aim


@expect({'test': 900})
def solve2(input):
    pos, dep, _ = template(input)
    return pos*dep
