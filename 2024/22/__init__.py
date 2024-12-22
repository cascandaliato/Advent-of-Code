from collections import defaultdict

from pyutils import *


def parse(lines):
    return map(int, lines)


def gen(secret, repeat=1):
    secrets = [secret]
    for _ in range(repeat):
        secret = ((secret * 64) ^ secret) % 16777216
        secret = ((secret // 32) ^ secret) % 16777216
        secret = ((secret * 2048) ^ secret) % 16777216
        secrets.append(secret)
    return secrets


@expect({"test1": 37327623})
def solve1(input):
    return sum(gen(secret, repeat=2000)[-1] for secret in input)


@expect({"test2": 23})
def solve2(input):
    seqs = defaultdict(lambda: 0)
    for secret in input:
        secrets = [s % 10 for s in gen(secret, repeat=2000)]
        diffs = [secrets[i] - secrets[i - 1] for i in range(1, 2001)]
        seen = set()
        for i in range(4, 2001):
            seq = tuple(diffs[i - 4 : i])
            if seq in seen:
                continue
            seen.add(seq)
            seqs[seq] += secrets[i]
    return max(seqs.values())
