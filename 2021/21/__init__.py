from functools import lru_cache
from itertools import product

from pyutils import *


def parse(lines):
    return [int(line.split(': ')[1]) for line in lines]


@expect({'test': 739785})
def solve1(starting_pos):
    pos, scores, player, rolls = starting_pos, [0, 0], 0, 0

    while max(scores) < 1000:
        pos[player] = (pos[player] + sum((rolls+i) %
                                         100 + 1 for i in range(3)) - 1) % 10 + 1
        scores[player] += pos[player]
        player = int(not player)
        rolls += 3
    return min(scores)*rolls


@expect({'test': 444356092776315})
def solve2(starting_pos):
    @lru_cache(maxsize=None)
    def wins(pos1, pos2, score1, score2, player):
        if max(score1, score2) >= 21:
            return (1, 0) if score1 > score2 else (0, 1)

        next_games = []
        for rolls in product([1, 2, 3], repeat=3):
            pos, scores = [pos1, pos2], [score1, score2]
            pos[player] = (pos[player] + sum(rolls) - 1) % 10 + 1
            scores[player] += pos[player]
            next_games.append((*pos, *scores, int(not(player))))
        return sum(wins(*next_game)[0] for next_game in next_games), \
            sum(wins(*next_game)[1] for next_game in next_games)

    return max(wins(*starting_pos, 0, 0, 0))
