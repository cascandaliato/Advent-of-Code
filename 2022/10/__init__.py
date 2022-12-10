from pyutils import *


def parse(lines):
    instructions = []
    for line in lines:
        instructions.append(0)
        if line.startswith('addx'):
            instructions.append(int(line.split()[1]))
    return instructions


def register_history(instructions):
    h = [1]
    for n in instructions:
        h.append(h[-1]+n)
    return h


@expect({'test': 13140})
def solve1(instructions):
    history = register_history(instructions)
    return sum((c+1)*history[c] for c in range(19, 220, 40))


def solve2(instructions):
    history = register_history(instructions)

    screen = []
    for c in range(240):
        if c % 40 in range(history[c]-1, history[c]+2):
            screen.append('#')
        else:
            screen.append('.')

    for i in range(0, 201, 40):
        print(''.join(screen[i:i+40]))
