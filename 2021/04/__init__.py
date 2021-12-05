from pyutils import *
from collections import defaultdict

BY_ROW, BY_COL = 0, 1


def parse(lines):
    draws, *boards = split_by_empty_line(lines)

    draws = [int(n) for n in draws[0].split(',')]
    boards = [[[int(n) for n in row.strip().split()]
               for row in board] for board in boards]

    n_to_position = defaultdict(set)
    for i, board in enumerate(boards):
        for r in range(5):
            for c in range(5):
                n_to_position[board[r][c]].add((i, r, c))

    countdown = [{BY_ROW: [5]*5, BY_COL:[5]*5} for _ in range(len(boards))]

    return (draws, boards, n_to_position, countdown)


def nth_winning_score(input, n):
    draws, boards, n_to_position, countdown = input
    boards_playing, won_counter = set(range(len(boards))), 0

    for d, draw in enumerate(draws):
        for board, row, col in n_to_position[draw]:
            if board not in boards_playing:
                continue
            countdown[board][BY_ROW][row] -= 1
            countdown[board][BY_COL][col] -= 1
            if countdown[board][BY_ROW][row] == 0 or countdown[board][BY_COL][col] == 0:
                boards_playing.remove(board)
                won_counter += 1
                if won_counter == n:
                    return draw * sum(n for row in boards[board] for n in row if n not in set(draws[:d+1]))


@expect({'test': 4512})
def solve1(input):
    return nth_winning_score(input, 1)


@expect({'test': 1924})
def solve2(input):
    return nth_winning_score(input, len(input[1]))
