import math
from pyutils import *


def parse(lines):
    seeds = [int(n) for n in lines[0].split(": ")[1].split()]
    maps = [[]]
    for line in lines[2:]:
        if line:
            maps[-1].append(line)
        else:
            maps.append([])
    for i in range(len(maps)):
        maps[i] = maps[i][1:]
        m = maps[i]
        for j, line in enumerate(m):
            m[j] = [int(n) for n in line.split()]
            m[j] = [
                m[j][1],
                m[j][1] + m[j][2] - 1,
                m[j][0] - m[j][1],
            ]
        m.sort()
    return seeds, maps


@expect({"test": 35})
def solve1(data):
    seeds, maps = data
    location = math.inf
    for seed in seeds:
        for m in maps:
            for l, r, d in m:
                if l <= seed <= r:
                    seed += d
                    break
        location = min(location, seed)
    return location


@expect({"test": 46})
def solve2(data):
    seeds, maps = data

    seeds = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    for m in maps:
        next_seeds = []
        for a, b in seeds:
            for l, r, d in m:
                if a > r:
                    continue
                if b < l:
                    next_seeds.append([a, b])
                    break
                if a < l:
                    next_seeds.append([a, l - 1])
                next_seeds.append([max(a, l) + d, min(b, r) + d])
                a, b = [max(a, r + 1), b]
                if a > b:
                    break
            if a <= b:
                next_seeds.append([a, b])
        seeds = next_seeds

    return min(a for a, _ in seeds)
