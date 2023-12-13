from pyutils import *


def parse(lines):
    return lines


move = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


def solve(keypad, start, instructions):
    r, c = start
    code = []
    for line in instructions:
        for m in line:
            r_next = r + move[m][0]
            c_next = c + move[m][1]
            if (
                r_next in range(len(keypad))
                and c_next in range(len(keypad[0]))
                and keypad[r_next][c_next] != " "
            ):
                r, c = r_next, c_next
        code.append(keypad[r][c])
    return "".join(code)


@expect({"test": "1985"})
def solve1(instructions):
    keypad = ["123", "456", "789"]
    return solve(keypad, (1, 1), instructions)


@expect({"test": "5DB3"})
def solve2(instructions):
    keypad = ["  1  ", " 234 ", "56789", " ABC ", "  D  "]
    return solve(keypad, (2, 0), instructions)
