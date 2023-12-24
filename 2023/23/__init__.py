from pyutils import *


def parse(grid):
    return grid


@expect({"test": 94})
def solve1(grid):
    longest = 0
    start, end = (0, 1), (len(grid) - 1, len(grid[0]) - 2)
    q = [(start, set())]
    while q:
        (r, c), visited = q.pop()
        if (r, c) == end:
            longest = max(longest, len(visited))
            continue
        next = []
        for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0)):
            next_r, next_c = r + dr, c + dc
            if (
                0 <= next_r < len(grid)
                and 0 <= next_c < len(grid[0])
                and (next_r, next_c) not in visited
                and (
                    grid[next_r][next_c] == "."
                    or (grid[next_r][next_c] == ">" and (dr, dc) == (0, 1))
                    or (grid[next_r][next_c] == "<" and (dr, dc) == (0, -1))
                    or (grid[next_r][next_c] == "^" and (dr, dc) == (-1, 0))
                    or (grid[next_r][next_c] == "v" and (dr, dc) == (1, 0))
                )
            ):
                next.append((next_r, next_c))
        for n in next:
            q.append((n, (visited.copy() if len(next) > 1 else visited).union({n})))
    return longest


@expect({"test": 154})
def solve2(grid):
    graph = dict()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                continue
            graph[(r, c)] = dict()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (
                    0 <= r + dr < len(grid)
                    and 0 <= c + dc < len(grid[0])
                    and grid[r + dr][c + dc] != "#"
                ):
                    graph[(r, c)][(r + dr, c + dc)] = 1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if len(neighbors := list(graph.get((r, c), {}).keys())) == 2:
                graph[neighbors[0]][neighbors[1]] = (
                    graph[neighbors[0]][(r, c)] + graph[(r, c)][neighbors[1]]
                )
                del graph[neighbors[0]][(r, c)]

                graph[neighbors[1]][neighbors[0]] = (
                    graph[neighbors[1]][(r, c)] + graph[(r, c)][neighbors[0]]
                )
                del graph[neighbors[1]][(r, c)]

                del graph[(r, c)]

    longest = 0
    start, end = (0, 1), (len(grid) - 1, len(grid[0]) - 2)
    q = [(start, 0, set())]
    while q:
        position, steps, visited = q.pop()
        if position == end:
            longest = max(longest, steps)
            continue
        for next_position, distance in graph[position].items():
            if next_position not in visited:
                q.append(
                    (next_position, steps + distance, visited.union({next_position}))
                )
    return longest
