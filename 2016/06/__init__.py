from collections import Counter

from pyutils import *


def parse(lines):
    return lines


def solve(input, nth=0):
    return "".join(
        [
            Counter(line[i] for line in input).most_common()[nth][0]
            for i in range(len(input[0]))
        ]
    )


@expect({"test": "easter"})
def solve1(input):
    return solve(input)


@expect({"test": "advent"})
def solve2(input):
    return solve(input, nth=-1)
