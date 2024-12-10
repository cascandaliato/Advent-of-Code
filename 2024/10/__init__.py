from pyutils import *


def parse(lines):
    trailheads = []
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "0":
                trailheads.append((r, c))
    return lines, trailheads


@expect({"test": 36})
def solve1(input):
    topo, trailheads = input

    score = 0
    for t in trailheads:
        q, nines = [t], set()
        while q:
            (r, c) = q.pop()
            if topo[r][c] == "9":
                nines.add((r, c))
                continue
            for dr, dc in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                if (
                    0 <= r + dr < len(topo)
                    and 0 <= c + dc < len(topo[0])
                    and int(topo[r + dr][c + dc]) == int(topo[r][c]) + 1
                ):
                    q.append((r + dr, c + dc))
        score += len(nines)
    return score


@expect({"test": 81})
def solve2(input):
    topo, trailheads = input

    score = 0
    for t in trailheads:
        q = [t]
        while q:
            (r, c) = q.pop()
            if topo[r][c] == "9":
                score += 1
                continue
            for dr, dc in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                if (
                    0 <= r + dr < len(topo)
                    and 0 <= c + dc < len(topo[0])
                    and int(topo[r + dr][c + dc]) == int(topo[r][c]) + 1
                ):
                    q.append((r + dr, c + dc))
    return score
