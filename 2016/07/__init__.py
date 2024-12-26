from pyutils import *


def parse(lines):
    return lines


@expect({"test1": 2})
def solve1(input):
    res = 0
    for ip in input:
        abba, hyper = False, False
        for i, c in enumerate(ip[:-3]):
            if c in ("[", "]"):
                hyper = c == "["
                continue
            else:
                if (
                    ip[i + 1] not in ("[", "]", ip[i])
                    and ip[i + 1] == ip[i + 2]
                    and ip[i] == ip[i + 3]
                ):
                    if hyper:
                        abba = False
                        break
                    else:
                        abba = True
        res += int(abba)
    return res


@expect({"test2": 3})
def solve2(input):
    res = 0
    for ip in input:
        aba, bab, hyper = set(), set(), False
        for i, c in enumerate(ip[:-2]):
            if c in ("[", "]"):
                hyper = c == "["
                continue
            else:
                if ip[i + 1] not in ("[", "]", ip[i]) and ip[i] == ip[i + 2]:
                    if hyper:
                        bab.add((ip[i + 1], ip[i]))
                    else:
                        aba.add((ip[i], ip[i + 1]))
        res += int(bool(aba.intersection(bab)))
    return res
