from collections import defaultdict

from pyutils import *


def parse(lines):
    status, instructions = split_by_empty_line(lines)
    stacks = defaultdict(list)
    for line in status[:-1]:
        for idx, crate in enumerate([line[i] for i in range(1, len(line), 4)]):
            if crate != " ":
                stacks[int(idx) + 1].insert(0, crate)
    return stacks, [ints(instruction.split(" ")[1::2]) for instruction in instructions]


def solve(stacks, instructions, get):
    for n, frm, to in instructions:
        stacks[to].extend(get(n, stacks[frm]))
    return "".join(s.pop() for _, s in sorted(stacks.items()))


@expect({'test': 'CMZ'})
def solve1(input):
    return solve(*input, lambda n, s: (s.pop() for _ in range(n)))


@expect({'test': 'MCD'})
def solve2(input):
    return solve(*input, lambda n, s: reversed(list(s.pop() for _ in range(n))))
