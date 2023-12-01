from pyutils import *


def parse(lines):
    return lines


@expect({"test1": 142})
def solve1(input):
    res = 0
    for line in input:
        digits = [d for d in line if d.isdigit()]
        res += int(digits[0] + digits[-1])
    return res


@expect({"test2": 281})
def solve2(input):
    trie = {}
    for w, v in [
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]:
        p = trie
        for c in w:
            p = p.setdefault(c, {})
        p["value"] = v

    res = 0
    for line in input:
        paths, digits = [trie], []
        for c in line:
            new_paths = [trie]
            if c.isdigit():
                digits.append(c)
            else:
                for p in paths:
                    if c not in p:
                        continue
                    p = p[c]
                    if "value" in p:
                        digits.append(str(p["value"]))
                    else:
                        new_paths.append(p)
            paths = new_paths
        res += int(digits[0] + digits[-1])
    return res
