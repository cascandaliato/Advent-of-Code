from collections import deque
from itertools import chain

from pyutils import *


def parse(lines):
    return (int(d) for d in lines[0])


@expect({"test": 1928})
def solve1(input):
    blocks, free_space, id, position = deque(), deque(), 0, 0
    for i, length in enumerate(input):
        if not length:
            continue
        if i % 2 == 0:
            for j in range(length):
                blocks.append((position + j, id))
            id += 1
        else:
            for j in range(length):
                free_space.append(position + j)
        position += length

    while free_space and blocks and free_space[0] < blocks[-1][0]:
        blocks.appendleft((free_space.popleft(), blocks.pop()[1]))

    return sum(i * id for i, id in blocks)


@expect({"test": 2858})
def solve2(input):
    files, free_space, id, position = [], [], 0, 0
    for i, length in enumerate(input):
        if not length:
            continue
        if i % 2 == 0:
            files.append((position, length, id))
            id += 1
        else:
            free_space.append((position, length))
        position += length

    free_space.reverse()
    files_moved = set()
    while free_space:
        for j in reversed(range(len(files))):
            if files[j][0] < free_space[-1][0]:
                free_space.pop()
                break

            if files[j][1] <= free_space[-1][1]:
                free_slot = free_space.pop()
                files_moved.add((free_slot[0], files[j][1], files[j][2]))
                if free_slot[1] > files[j][1]:
                    free_space.append(
                        (free_slot[0] + files[j][1], free_slot[1] - files[j][1])
                    )
                files.pop(j)
                break
        else:
            free_space.pop()

    return sum(
        f[2] * (f[0] * f[1] + f[1] * (f[1] - 1) // 2) for f in chain(files, files_moved)
    )
