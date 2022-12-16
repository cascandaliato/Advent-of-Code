import re

from pyutils import *


def manhattan(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def parse(lines):
    data = []
    for line in lines:
        coords = list(int(n) for n in re.findall(r'-?\d+', line))
        sensor, beacon = (coords[0], coords[1]), (coords[2], coords[3])
        distance = manhattan(sensor, beacon)
        data.append((sensor, beacon, distance))
    return data


# @expect({'test': 26})
def solve1(data):
    # Y = 10
    Y = 2_000_000
    excluded = set()
    for sensor, _, distance in data:
        dy = abs(sensor[1]-Y)
        if distance >= dy:
            excluded.update((x, Y) for x in range(
                sensor[0] - distance+dy, sensor[0]+distance-dy+1, 1))
    return len(excluded.difference(set(b for _, b, _ in data)))


# @expect({'test': 56000011})
def solve2(data):
    # LIMIT = 20
    LIMIT = 4_000_000
    beacons = set(b for _, b, _ in data)

    def valid(pos):
        return 0 <= pos[0] <= LIMIT and 0 <= pos[1] <= LIMIT and pos not in beacons and all(manhattan(pos, s) > d for s, _, d in data)

    for sensor, _, distance in data:
        for dy in range(distance+2):
            for pos in [(sensor[0]+dy, sensor[1]+distance+1-dy),
                        (sensor[0]+dy, sensor[1]-distance-1+dy),
                        (sensor[0]-dy, sensor[1]+distance+1-dy),
                        (sensor[0]-dy, sensor[1]-distance-1+dy),
                        ]:
                if valid(pos):
                    return pos[0]*4_000_000+pos[1]
    return None
