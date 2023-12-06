import math

from pyutils import *


def parse(lines):
    return [
        (int(lines[0].split()[i]), int(lines[1].split()[i]))
        for i in range(1, len(lines[0].split()))
    ]


@expect({"test": 288})
def solve1(races):
    ans = 1
    for t, d in races:
        ans *= (
            math.ceil((t + math.sqrt(t * t - 4 * d)) / 2 - 1)
            - math.floor((t - math.sqrt(t * t - 4 * d)) / 2 + 1)
            + 1
        )
    return ans


@expect({"test": 71503})
def solve2(races):
    return solve1(
        [tuple(int("".join(str(race[i]) for race in races)) for i in range(2))]
    )
