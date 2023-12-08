import math

from pyutils import *


def parse(lines):
    graph = {}
    for line in lines[2:]:
        src, lr = line.split(" = ")
        l, r = lr[1:-1].split(", ")
        graph[src] = {"L": l, "R": r}
    return lines[0], graph


def step(instructions):
    i = 0
    while True:
        for instr in instructions:
            i += 1
            yield i, instr


def solve(data, src, *dsts):
    instructions, graph = data
    curr = src
    for n, instr in step(instructions):
        curr = graph[curr][instr]
        if curr in dsts:
            return n


@expect({"test1": 2, "test2": 6})
def solve1(data):
    return solve(data, "AAA", "ZZZ")


@expect({"test3": 6})
def solve2(data):
    _, graph = data
    srcs = [a for a in graph if a.endswith("A")]
    dsts = [z for z in graph if z.endswith("Z")]
    return math.lcm(*(solve(data, src, *dsts) for src in srcs))
