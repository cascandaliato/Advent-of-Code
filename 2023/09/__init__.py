from pyutils import *


def parse(lines):
    return [[int(n) for n in line.split()] for line in lines]


def calc_diffs(seq):
    diffs = [seq]
    while not all(n == 0 for n in diffs[-1]):
        diffs.append([])
        for i in range(1, len(diffs[-2])):
            diffs[-1].append(diffs[-2][i] - diffs[-2][i - 1])
    return diffs


def solve(seqs, combine):
    ans = 0
    for seq in seqs:
        diffs, curr = calc_diffs(seq), 0
        for i in reversed(range(1, len(diffs))):
            curr = combine(diffs[i - 1], curr)
        ans += curr
    return ans


@expect({"test": 114})
def solve1(seqs):
    return solve(seqs, lambda seq, curr: seq[-1] + curr)


@expect({"test": 2})
def solve2(seqs):
    return solve(seqs, lambda seq, curr: seq[0] - curr)
