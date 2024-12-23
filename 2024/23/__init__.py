from collections import defaultdict
from itertools import combinations

from pyutils import *


def parse(lines):
    adj = defaultdict(set)
    for line in lines:
        a, b = line.split("-")
        adj[a].add(b)
        adj[b].add(a)
    return adj


def find_cliques(adj):
    cliques = []

    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    def bron_kerbosch(r, p, x):
        if not p and not x:
            cliques.append(r)
        while p:
            v = p.pop()
            bron_kerbosch(r | {v}, (p | {v}) & adj[v], x & adj[v])
            x |= {v}

    bron_kerbosch(set(), set(adj.keys()), set())
    return cliques


@expect({"test": 7})
def solve1(input):
    combos = set()
    for clique in find_cliques(input):
        for combo in combinations(clique, 3):
            if any(v.startswith("t") for v in combo):
                combos.add(tuple(sorted(combo)))
    return len(combos)


@expect({"test": "co,de,ka,ta"})
def solve2(input):
    max_clique = tuple()
    for clique in find_cliques(input):
        if len(clique) > len(max_clique):
            max_clique = clique
    return ",".join(sorted(max_clique))
