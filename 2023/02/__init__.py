from collections import defaultdict
from pyutils import *


def parse(lines):
    games = []
    for game in [line.split(": ")[1].split("; ") for line in lines]:
        mins = defaultdict(lambda: 0)
        for reveal in game:
            for r in reveal.split(", "):
                n, c = r.split(" ")
                mins[c] = max(mins[c], int(n))
        games.append((mins["red"], mins["green"], mins["blue"]))
    return games


@expect({"test": 8})
def solve1(games):
    bag = (12, 13, 14)
    return sum(
        i + 1
        for i, game in enumerate(games)
        if all(game[j] <= bag[j] for j in range(2))
    )


@expect({"test": 2286})
def solve2(games):
    return sum(g[0] * g[1] * g[2] for g in games)
