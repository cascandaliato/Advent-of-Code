from collections import defaultdict
from graphlib import TopologicalSorter

from pyutils import *


def parse(lines):
    rules = defaultdict(set)
    for i, line in enumerate(lines):
        if not line:
            break
        a, b = line.split("|")
        rules[a].add(b)

    updates = []
    for i in range(i + 1, len(lines)):
        updates.append(lines[i].split(","))

    return rules, updates


def is_correctly_ordered(update, rules):
    seen = set()
    for n in update:
        if rules[n].intersection(seen):
            return False
        seen.add(n)
    return True


@expect({"test": 143})
def solve1(input):
    rules, updates = input

    res = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            res += int(update[len(update) // 2])

    return res


@expect({"test": 123})
def solve2(input):
    rules, updates = input

    res = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            continue
        update, g = set(update), {}
        for n in update:
            g[n] = rules.get(n, set()).intersection(update)
        topo = list(TopologicalSorter(g).static_order())
        res += int(topo[len(topo) // 2])
    return res
