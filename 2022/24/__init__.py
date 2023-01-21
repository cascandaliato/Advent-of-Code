import math

from pyutils import *


class V(tuple):
    def __new__(cls, *elements):
        return super(V, cls).__new__(cls, tuple(elements))

    def __add__(self, o):
        return V(*[a + o[i] for i, a in enumerate(self)])


# def parse(lines):
#     start = V(-1, next(iter(c for c, v in enumerate(lines[0]) if v == "."))-1)
#     end = V(len(lines) - 2,
#             next(iter(c for c, v in enumerate(lines[-1]) if v == "."))-1)

#     # directions = {"^": V(-1, 0), "v": V(+1, 0), "<": V(0, -1), ">": V(0, +1)}
#     # winds = set()
#     # for r, line in enumerate(lines[1:-1]):
#     #     for c, v in enumerate(line[1:-1]):
#     #         if v != ".":
#     #             winds.add((V(r + 1, c + 1), directions[v]))

#     # return (winds, width, height, start, end)
#     return [line[1:-1] for line in lines[1:-1]], start, end


# def solve(grid, start, end, t0):
#     height, width = len(grid), len(grid[1])
#     T = height*width//math.gcd(height, width)

#     q, visited = [(t0, start)], set()
#     while q:
#         t, pos = q.pop()

#         if (t % T, pos) in visited:
#             continue
#         visited.add((t % T, pos))

#         if pos == end:
#             return t

#         t += 1
#         for delta in (V(0, 0), V(0, 1), V(0, -1), V(1, 0), V(-1, 0)):
#             r, c = pos+delta
#             if (r, c) in (start, end) or (0 <= r < height and 0 <= c < width and grid[r][(c-t) % width] != '>' and grid[r][(c+t) % width] != '<' and grid[(r-t) % height][c] != 'v' and grid[(r+t) % height][c] != '^'):
#                 q.insert(0, (t, V(r, c)))

def parse(lines):
    start = V(-1, next(iter(c for c, v in enumerate(lines[0]) if v == "."))-1)
    end = V(len(lines) - 2,
            next(iter(c for c, v in enumerate(lines[-1]) if v == "."))-1)

    directions = {"^": V(-1, 0), "v": V(+1, 0), "<": V(0, -1), ">": V(0, +1)}
    winds = set()
    for r, line in enumerate(lines[1:-1]):
        for c, v in enumerate(line[1:-1]):
            if v != ".":
                winds.add((V(r, c), directions[v]))

    width, height = len(lines[0])-2, len(lines)-2
    return winds, width, height, start, end


def solve(winds, width, height, start, end, t0=0):
    T = height*width//math.gcd(height, width)
    q, visited = [(t0, start)], set()
    while q:
        t, pos = q.pop()

        if (t % T, pos) in visited:
            continue
        visited.add((t % T, pos))

        if pos == end:
            return t

        t += 1
        for delta in (V(0, 0), V(0, 1), V(0, -1), V(1, 0), V(-1, 0)):
            r, c = pos+delta
            if (r, c) in (start, end) or (0 <= r < height and 0 <= c < width) and ((r, (c-t) % width), (0, 1)) not in winds and ((r, (c+t) % width), (0, -1)) not in winds and (((r-t) % height, c), (1, 0)) not in winds and (((r+t) % height, c), (-1, 0)) not in winds:
                q.insert(0, (t, V(r, c)))


@ expect({'test': 18})
def solve1(input):
    return solve(*input)


@ expect({'test': 54})
def solve2(input):
    winds, width, height, start, end = input
    return solve(*input, solve(winds, width, height, end, start, solve(*input)))
