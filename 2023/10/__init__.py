from pyutils import *


N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
symbols = {
    "|": {N: N, S: S},
    "-": {E: E, W: W},
    "L": {S: E, W: N},
    "J": {E: N, S: W},
    "7": {N: W, E: S},
    "F": {N: E, W: S},
}


def parse(lines):
    tiles = [list(line) for line in lines]
    start = next(
        (r, c)
        for r in range(len(tiles))
        for c in range(len(tiles[0]))
        if tiles[r][c] == "S"
    )
    return tiles, start


def get_loop(tiles, start):
    q = [
        ([start], direction, (start[0] + direction[0], start[1] + direction[1]))
        for direction in [N, S, E, W]
    ]
    while q:
        path, direction, position = q.pop()
        if (
            position[0] < 0
            or position[0] >= len(tiles)
            or position[1] < 0
            or position[1] >= len(tiles[0])
        ):
            continue
        symbol = tiles[position[0]][position[1]]
        if symbol == ".":
            continue
        if symbol == "S":
            return path
        if direction in symbols[symbol]:
            path.append(position)
            direction = symbols[symbol][direction]
            q.append(
                (
                    path,
                    direction,
                    (position[0] + direction[0], position[1] + direction[1]),
                )
            )


@expect({"test1": 4, "test2": 4, "test3": 8})
def solve1(data):
    return len(get_loop(*data)) // 2


@expect({"test1": 1, "test4": 4, "test5": 8, "test6": 10})
def solve2(data):
    tiles, start = data
    loop = get_loop(tiles, start)

    # replace S with appropriate pipe
    a = (start[0] - loop[-1][0], start[1] - loop[-1][1])
    b = (start[0] - loop[1][0], start[1] - loop[1][1])
    for symbol, transforms in symbols.items():
        if transforms == {a: (-b[0], -b[1]), b: (-a[0], -a[1])}:
            tiles[start[0]][start[1]] = symbol
            break

    count = 0
    for r in range(len(tiles)):
        inside, up = False, False
        for c in range(len(tiles[0])):
            if (r, c) in loop:
                match tiles[r][c]:
                    case "|":
                        inside = not inside
                    case "L":
                        up = False
                    case "F":
                        up = True
                    case "7":
                        if not up:
                            inside = not inside
                    case "J":
                        if up:
                            inside = not inside
            elif inside:
                count += 1
    return count
