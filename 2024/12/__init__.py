from collections import deque

from pyutils import *


def parse(lines):
    return lines


@expect({"test1": 140, "test2": 772, "test3": 1930})
def solve1(input):
    price, visited = 0, set()

    for r0 in range(len(input)):
        for c0 in range(len(input[0])):
            if (r0, c0) in visited:
                continue

            q, area, sides = deque([(r0, c0)]), 0, 0
            while q:
                r, c = q.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                area += 1
                for dr, dc in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
                    if (
                        0 <= r + dr < len(input)
                        and 0 <= c + dc < len(input[0])
                        and input[r + dr][c + dc] == input[r][c]
                    ):
                        q.appendleft((r + dr, c + dc))
                    else:
                        sides += 1
            price += area * sides

    return price


@expect({"test1": 80, "test2": 436, "test3": 1206, "test4": 236, "test5": 368})
def solve2(input):
    price, visited = 0, set()

    for r0 in range(len(input)):
        for c0 in range(len(input[0])):
            if (r0, c0) in visited:
                continue

            q, area, segments = deque([(r0, c0)]), 0, set()
            while q:
                r, c = q.pop()
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                area += 1
                for dr, dc in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
                    if (
                        0 <= r + dr < len(input)
                        and 0 <= c + dc < len(input[0])
                        and input[r + dr][c + dc] == input[r][c]
                    ):
                        q.appendleft((r + dr, c + dc))
                    else:
                        segments.add(((r, c), (r + dr, c + dc)))

            sides = 0
            for (r1, c1), (r2, c2) in sorted(segments):
                if (r1 != r2 and ((r1, c1 + 1), (r2, c2 + 1)) not in segments) or (
                    c1 != c2 and ((r1 + 1, c1), (r2 + 1, c2)) not in segments
                ):
                    sides += 1
            price += area * sides

    return price
