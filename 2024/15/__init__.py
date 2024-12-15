from itertools import count

from pyutils import *


def parse(lines):
    warehouse, robot, moves = [], None, None
    for i, line in enumerate(lines):
        if not line:
            moves = "".join(lines[i + 1 :])
            break
        warehouse.append(list(line))
        for j in range(len(line)):
            if line[j] == "@":
                robot = [i, j]
    return warehouse, robot, moves


directions = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}


@expect({"test1": 2028, "test2": 10092})
def solve1(input):
    warehouse, robot, moves = input
    for move in moves:
        (dr, dc), can_move = directions[move], False
        for i in count(start=1):
            if (tile := warehouse[robot[0] + i * dr][robot[1] + i * dc]) in (".", "#"):
                can_move = tile == "."
                break

        if can_move:
            for j in reversed(range(i)):
                warehouse[robot[0] + (j + 1) * dr][robot[1] + (j + 1) * dc] = warehouse[
                    robot[0] + j * dr
                ][robot[1] + j * dc]
            warehouse[robot[0]][robot[1]] = "."
            robot = [robot[0] + dr, robot[1] + dc]

    res = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == "O":
                res += c + 100 * r
    return res


wider = {"#": "##", "O": "[]", ".": "..", "@": "@."}


@expect({"test2": 9021})
def solve2(input):
    warehouse, robot, moves = input
    for i, row in enumerate(warehouse):
        warehouse[i] = [t for tile in row for t in wider[tile]]
    robot[1] *= 2

    for move in moves:
        (dr, dc), can_move = directions[move], False

        if dc:
            for i in count(start=1):
                if (tile := warehouse[robot[0]][robot[1] + i * dc]) in (
                    ".",
                    "#",
                ):
                    can_move = tile == "."
                    break

            if can_move:
                for j in reversed(range(i)):
                    warehouse[robot[0]][robot[1] + (j + 1) * dc] = warehouse[robot[0]][
                        robot[1] + (j) * dc
                    ]
                warehouse[robot[0]][robot[1]] = "."
                robot = [robot[0], robot[1] + dc]

        if dr:
            pushers = [{robot[1]}]
            for i in count(start=1):
                pushed = set()

                if any(warehouse[robot[0] + i * dr][j] == "#" for j in pushers[-1]):
                    can_move = False
                    break

                if all(warehouse[robot[0] + i * dr][j] == "." for j in pushers[-1]):
                    can_move = True
                    break

                for p in pushers[-1]:
                    if warehouse[robot[0] + i * dr][p] == "]":
                        pushed.add(p - 1)
                        pushed.add(p)
                    if warehouse[robot[0] + i * dr][p] == "[":
                        pushed.add(p)
                        pushed.add(p + 1)
                pushers.append(pushed)

            if can_move:
                for j in reversed(range(i)):
                    pushed = pushers.pop()
                    for p in pushed:
                        warehouse[robot[0] + (j + 1) * dr][p] = warehouse[
                            robot[0] + j * dr
                        ][p]
                        warehouse[robot[0] + j * dr][p] = "."
                warehouse[robot[0]][robot[1]] = "."
                robot = (robot[0] + dr, robot[1])

    res = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == "[":
                res += c + 100 * r
    return res
