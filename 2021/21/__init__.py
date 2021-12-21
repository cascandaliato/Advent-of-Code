from itertools import product

from pyutils import *


def parse(lines):
    return [int(line.split(': ')[1]) for line in lines]


def t(game):
    return game[0][0], game[0][1], game[1][0], game[1][1], game[2]


@expect({'test': 739785})
def solve1(starting_pos):
    pos, scores, player, rolls = starting_pos, [0, 0], 0, 0

    while max(scores) < 1000:
        pos[player] = (pos[player] + sum((rolls+i) %
                                         100 + 1 for i in range(3)) - 1) % 10 + 1
        scores[player] += pos[player]
        player = -player+1
        rolls += 3
    return min(scores)*rolls


@expect({'test': 444356092776315})
def solve2(starting_pos):
    initial_state = (starting_pos, [0, 0], 0)
    games, outcomes = [initial_state], {}
    while games:
        game = games.pop()
        if t(game) in outcomes:
            continue

        pos, scores, player = game
        if max(scores) >= 21:
            outcomes[t(game)] = (1, 0) if scores[0] > scores[1] else (0, 1)
        else:
            next_games = []
            for rolls in product([1, 2, 3], repeat=3):
                alt_pos, alt_scores = pos.copy(), scores.copy()
                alt_pos[player] = (pos[player] + sum(rolls) - 1) % 10 + 1
                alt_scores[player] += alt_pos[player]
                next_games.append((alt_pos, alt_scores, -player+1))
            if all(t(next_game) in outcomes for next_game in next_games):
                outcomes[t(game)] = tuple(sum(t) for t in zip(
                    *[outcomes[t(next_game)] for next_game in next_games]))
            else:
                games.append(game)
                games.extend(next_games)
    return max(outcomes[t(initial_state)])
