from pyutils import *


def parse(lines):
    bricks = set()
    for line in lines:
        coords = list(map(lambda c: (int(c.split(',')[0]), int(
            c.split(',')[1])), line.split(' -> ')))
        for i in range(len(coords)-1):
            r_min, r_max = min(coords[i][0], coords[i+1]
                               [0]), max(coords[i][0], coords[i+1][0])
            d_min, d_max = min(coords[i][1], coords[i+1]
                               [1]), max(coords[i][1], coords[i+1][1])
            for r in range(r_min, r_max+1, 1):
                for d in range(d_min, d_max+1, 1):
                    bricks.add((r, d))
    return bricks


@expect({'test': 24})
def solve1(bricks):
    abyss, sand = max(b[1] for b in bricks), set()
    while True:
        pos = (500, 0)
        while True:
            if pos[1] == abyss:
                return len(sand)
            if (pos[0], pos[1]+1) not in bricks and (pos[0], pos[1]+1) not in sand:
                pos = (pos[0], pos[1]+1)
            elif (pos[0]-1, pos[1]+1) not in bricks and (pos[0]-1, pos[1]+1) not in sand:
                pos = (pos[0]-1, pos[1]+1)
            elif (pos[0]+1, pos[1]+1) not in bricks and (pos[0]+1, pos[1]+1) not in sand:
                pos = (pos[0]+1, pos[1]+1)
            else:
                sand.add(pos)
                break


@expect({'test': 93})
def solve2(bricks):
    floor, sand = max(b[1] for b in bricks)+2, set()
    q = [(500, 0)]
    while q:
        pos = q.pop()
        if pos in bricks or pos in sand or pos[1] == floor:
            continue
        sand.add(pos)
        q.extend([(pos[0]-1, pos[1]+1), (pos[0], pos[1]+1), (pos[0]+1, pos[1]+1)])
    return len(sand)
