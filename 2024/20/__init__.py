from pyutils import *


def parse(lines):
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == "S":
                start = (r, c)
            if ch == "E":
                end = (r, c)
    return lines, start, end


# @expect({"test": None})
def solve1(input, cheat_length=2):
    grid, start, end = input

    q, visited, parents = [start], set(), {}
    while q:
        r, c = q.pop()

        if (r, c) == end:
            break

        visited.add((r, c))

        for dr, dc in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
            if (
                0 <= r + dr < len(grid)
                and 0 <= c + dc < len(grid[0])
                and grid[r][c] != "#"
                and (r + dr, c + dc) not in visited
            ):
                parents[(r + dr, c + dc)] = (r, c)
                q.append((r + dr, c + dc))

    node, path = end, [end]
    while node in parents:
        path.append(parents[node])
        node = parents[node]
    path.reverse()

    res = 0
    for i, (ra, ca) in enumerate(path):
        for j, (rb, cb) in enumerate(path[i + 1 :], start=i + 1):
            if (
                abs(rb - ra) + abs(cb - ca) <= cheat_length
                and j - i - (abs(rb - ra) + abs(cb - ca)) >= 100
            ):
                res += 1
    return res


# @expect({"test": None})
def solve2(input):
    return solve1(input, cheat_length=20)
