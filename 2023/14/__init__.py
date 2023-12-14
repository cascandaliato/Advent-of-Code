from pyutils import *


def parse(lines):
    return [list(line) for line in lines]


def tilt_north(platform):
    for c in range(len(platform[0])):
        rocks = 0
        for r in reversed(range(len(platform))):
            match platform[r][c]:
                case "#":
                    for i in range(rocks):
                        platform[r + 1 + i][c] = "O"
                    rocks = 0
                case "O":
                    platform[r][c] = "."
                    rocks += 1
        if rocks:
            for i in range(rocks):
                platform[i][c] = "O"


def rot90(platform):
    rotated = [[None] * len(platform) for _ in range(len(platform[0]))]
    for r in range(len(platform)):
        for c in range(len(platform[0])):
            rotated[c][len(platform[0]) - 1 - r] = platform[r][c]
    return rotated


def state(platform):
    return tuple(tuple(row) for row in platform)


def load(platform):
    return sum(
        len(platform) - r
        for r in range(len(platform))
        for c in range(len(platform[0]))
        if platform[r][c] == "O"
    )


@expect({"test": 136})
def solve1(platform):
    tilt_north(platform)
    return load(platform)


@expect({"test": 64})
def solve2(platform):
    states = [state(platform)]

    cycles = 1000000000
    for cycle in range(cycles):
        for _ in range(4):
            tilt_north(platform)
            platform = rot90(platform)
        current_state = state(platform)
        try:
            i = states.index(current_state)
            final_state = states[i + (cycles - i) % (cycle + 1 - i)]
            return load(final_state)
        except ValueError:
            states.append(current_state)
