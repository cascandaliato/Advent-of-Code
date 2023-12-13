from pyutils import *


def parse(lines):
    patterns = [[]]
    for line in lines:
        if line:
            patterns[-1].append(line)
        else:
            patterns.append([])
    return patterns


def has_v_reflection(pattern, with_smudge=False):
    def is_v_reflection(row, candidate, smudge_fixed):
        diffs = 0
        rng = min(candidate, len(row) - candidate)
        for i in range(rng):
            if row[candidate - 1 - i] != row[candidate + i]:
                diffs += 1
        if diffs == 0:
            return True, smudge_fixed
        elif with_smudge and diffs == 1 and not smudge_fixed:
            return True, True
        else:
            return False, False

    candidates = [(n, False) for n in range(1, len(pattern[0]))]
    for row in pattern:
        candidates_new = []
        for candidate, smudge_fixed in candidates:
            is_reflection, smudge_fixed_new = is_v_reflection(
                row, candidate, smudge_fixed
            )
            if is_reflection:
                candidates_new.append((candidate, smudge_fixed_new))
        candidates = candidates_new

    for candidate, smudge_fixed in candidates:
        if smudge_fixed == with_smudge:
            return candidate
    return 0


def transpose(pattern):
    transposed = [[] for _ in range(len(pattern[0]))]
    for r in range(len(pattern)):
        for c in range(len(pattern[0])):
            transposed[c].append(pattern[r][c])
    return transposed


def solve(patterns, with_smudge=False):
    ans = 0
    for pattern in patterns:
        if n := has_v_reflection(pattern, with_smudge):
            ans += n
        else:
            ans += has_v_reflection(transpose(pattern), with_smudge) * 100
    return ans


@expect({"test": 405})
def solve1(patterns):
    return solve(patterns)


@expect({"test": 400})
def solve2(patterns):
    return solve(patterns, with_smudge=True)
