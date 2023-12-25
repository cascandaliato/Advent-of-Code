import networkx as nx
from pyutils import *


def parse(lines):
    graph = nx.Graph()
    for line in lines:
        a, bs = line.split(": ")
        for b in bs.split():
            graph.add_edge(a, b)
    return graph


@expect({"test": 54})
def solve1(graph):
    # https://en.wikipedia.org/wiki/Stoer%E2%80%93Wagner_algorithm
    _, (p1, p2) = nx.stoer_wagner(graph)
    return len(p1) * len(p2)
