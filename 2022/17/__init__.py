from pyutils import *

rocks = ((0, 1, 2, 3), (1, 1j, 1+1j, 2+1j, 1+2j),
         (0, 1, 2, 2+1j, 2+2j), (0, 1j, 2j, 3j), (0, 1, 1j, 1+1j))
heights = [max(r.imag for r in rock)+1 for rock in rocks]
directions = {'<': -1, '>': +1}


def parse(lines):
    return [directions[d] for d in lines[0]]


def is_valid(pos, chamber):
    return pos.real in range(7) and pos.imag > 0 and pos not in chamber


def can_move(rock, pos, direction, chamber):
    return all(
        is_valid(pos+r+direction, chamber) for r in rock)


def dfs(chamber, top):
    q = [complex(i, top)
         for i in range(7) if is_valid(complex(i, top), chamber)]
    visited, empty = set(), set()
    while q:
        pos = q.pop()
        if pos in visited:
            continue
        visited.add(pos)
        if is_valid(pos, chamber):
            empty.add((pos.real, top-pos.imag))
            q.extend([pos-1, pos+1, pos-1j])
    return tuple(sorted(empty))


def solve(jets, steps):
    cache = {}
    chamber, top, rock_idx, jet_idx = set(), 0, 0, 0
    for i in range(steps):
        reachables = dfs(chamber, top)
        if (rock_idx, jet_idx, reachables) in cache:
            i_prev, top_prev = cache[(rock_idx, jet_idx, reachables)]
            quotient, remainder = divmod(steps-i, i-i_prev)
            if remainder == 0:
                return int((top + (top-top_prev)*quotient))
        else:
            cache[(rock_idx, jet_idx, reachables)] = (i, top)

        rock, rock_height = rocks[rock_idx], heights[rock_idx]
        rock_idx = (rock_idx+1) % len(rocks)
        pos = complex(2, top+4)
        while True:
            jet = jets[jet_idx]
            jet_idx = (jet_idx+1) % len(jets)
            if can_move(rock, pos, jet, chamber):
                pos += jet
            if can_move(rock, pos, -1j, chamber):
                pos += -1j
            else:
                chamber |= {pos+r for r in rock}
                top = max(top, pos.imag+rock_height-1)
                break
    return int(top)


@expect({'test': 3068})
def solve1(jets):
    return solve(jets, 2022)


@expect({'test': 1514285714288})
def solve2(jets):
    return solve(jets, 1_000_000_000_000)
