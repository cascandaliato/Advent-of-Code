from heapq import heappop, heappush

from pyutils import *


def parse(lines):
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "S":
                start = (r, c)
            if ch == "E":
                end = (r, c)
    return lines, start, end


directions = ((0, 1), (-1, 0), (0, -1), (1, 0))


@expect({"test1": 7036, "test2": 11048})
def solve1(input):
    maze, start, end = input
    q, visited = [(0, start, 0)], set()
    while q:
        score, position, direction = heappop(q)
        if position == end:
            return score_new
        if position in visited:
            continue
        visited.add(position)

        for i in (0, 1, -1):
            direction_new = (direction + i) % 4
            dr, dc = directions[direction_new]
            r_new, c_new = position[0] + dr, position[1] + dc

            if maze[r_new][c_new] == "#":
                continue

            score_new = score + 1 + abs(i) * 1000

            heappush(q, (score_new, (r_new, c_new), direction_new))


@expect({"test1": 45, "test2": 64})
def solve2(input):
    best_score = solve1(input)

    maze, start, end = input
    q, visited, best_seats = [(0, start, 0, {start})], set(), set()
    while q:
        score, (r, c), direction, path = heappop(q)
        if score > best_score:
            return len(best_seats)
        visited.add((r, c, direction))

        for i in (0, 1, -1):
            direction_new = (direction + i) % 4
            dr, dc = directions[direction_new]
            r_new, c_new = r + dr, c + dc

            if maze[r_new][c_new] == "#":
                continue

            if (r_new, c_new) == end:
                best_seats.update(path)
                best_seats.add(end)
                continue
            if (r_new, c_new, direction_new) in visited:
                continue

            score_new = score + 1 + abs(i) * 1000
            heappush(
                q, (score_new, (r_new, c_new), direction_new, path | {(r_new, c_new)})
            )
