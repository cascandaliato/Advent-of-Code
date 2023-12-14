from pyutils import *


def parse(lines):
    patterns = [[]]
    for line in lines:
        if line:
            patterns[-1].append(line)
        else:
            patterns.append([])
    return patterns


def has_v_reflection(pattern, smudges=0):
    def is_v_reflection(row, candidate, smudges_left):
        rng = min(candidate, len(row) - candidate)
        for i in range(rng):
            if row[candidate - 1 - i] != row[candidate + i]:
                smudges_left -= 1
        return smudges_left

    candidates = [(n, smudges) for n in range(1, len(pattern[0]))]
    for row in pattern:
        candidates_new = []
        for candidate, smudges_left in candidates:
            smudges_left = is_v_reflection(row, candidate, smudges_left)
            if smudges_left >= 0:
                candidates_new.append((candidate, smudges_left))
        candidates = candidates_new

    for candidate, smudges_left in candidates:
        if smudges_left == 0:
            return candidate
    return 0


def transpose(pattern):
    return list(zip(*pattern))


def solve(patterns, smudges=0):
    ans = 0
    for pattern in patterns:
        if n := has_v_reflection(pattern, smudges):
            ans += n
        else:
            ans += has_v_reflection(transpose(pattern), smudges) * 100
    return ans


@expect({"test": 405})
def solve1(patterns):
    return solve(patterns)


@expect({"test": 400})
def solve2(patterns):
    return solve(patterns, smudges=1)
