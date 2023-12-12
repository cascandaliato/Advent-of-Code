from functools import cache
from pyutils import *


def parse(lines):
    data = []
    for line in lines:
        row, groups = line.split(" ")
        data.append((row, [int(n) for n in groups.split(",")]))
    return data


def solve(row, groups):
    @cache
    def count(i=0, g=0, adj=0):
        if i >= len(row):
            return int(
                (adj == 0 and g >= len(groups))
                or (g == len(groups) - 1 and adj == groups[g])
            )

        if adj > 0 and (g >= len(groups) or adj > groups[g]):
            return 0

        match row[i]:
            case ".":
                if adj == 0:
                    return count(i + 1, g, 0)
                elif adj == groups[g]:
                    return count(i + 1, g + 1, 0)
                else:
                    return 0
            case "#":
                return count(i + 1, g, adj + 1)
            case "?":
                c = count(i + 1, g, adj + 1)
                if adj == 0:
                    c += count(i + 1, g, 0)
                elif adj == groups[g]:
                    c += count(i + 1, g + 1, 0)
                return c

    return count()


@expect({"test": 21})
def solve1(data):
    return sum(solve(*d) for d in data)


@expect({"test": 525152})
def solve2(data):
    return solve1([("?".join([row] * 5), groups * 5) for row, groups in data])
