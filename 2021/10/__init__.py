from statistics import median

from pyutils import *

closing = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
}


def score(line):
    opens = []
    for char in line:
        if char in closing:
            expected, score = closing[char]
            if not opens or opens.pop() != expected:
                return -score
        else:
            opens.append(char)
    score = 0
    for char in reversed(opens):
        score = score*5 + '([{<'.index(char)+1
    return score


@expect({'test': 26397})
def solve1(input):
    return sum(-score(line) for line in input if score(line) < 0)


@expect({'test': 288957})
def solve2(input):
    return median(score(line) for line in input if score(line) > 0)
