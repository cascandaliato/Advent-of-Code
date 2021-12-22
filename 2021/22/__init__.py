from math import inf

from pyutils import *


def parse(lines):
    instructions = []
    for line in lines:
        switch, xyz = line.split(' ')
        instructions.append(
            (True if switch == 'on' else False,
             *[tuple(
                 int(n) for n in d[2:].split('..')) for d in xyz.split(',')])
        )
    return instructions


def get_intersection(ranges1, ranges2):
    (xmin1, xmax1), (ymin1, ymax1), (zmin1, zmax1) = ranges1
    (xmin2, xmax2), (ymin2, ymax2), (zmin2, zmax2) = ranges2

    xmin, xmax = max(xmin1, xmin2), min(xmax1, xmax2)
    ymin, ymax = max(ymin1, ymin2), min(ymax1, ymax2)
    zmin, zmax = max(zmin1, zmin2), min(zmax1, zmax2)

    return ((xmin, xmax), (ymin, ymax), (zmin, zmax)) if xmin <= xmax and ymin <= ymax and zmin <= zmax else None


class Cuboid:
    def __init__(self, ranges):
        self.ranges = ranges
        self.removed_intersections = []

    def remove_intersection(self, ranges):
        intersection = get_intersection(self.ranges, ranges)

        if intersection:
            for remint in self.removed_intersections:
                remint.remove_intersection(intersection)
            self.removed_intersections.append(Cuboid(intersection))

    def size(self):
        (xmin, xmax), (ymin, ymax), (zmin, zmax) = self.ranges
        return (xmax-xmin+1)*(ymax-ymin+1)*(zmax-zmin+1) - sum(r.size() for r in self.removed_intersections)


def solve(instructions, clamp=((-inf, +inf), (-inf, +inf), (-inf, +inf))):
    cuboids = []
    for on, *ranges in instructions:
        ranges = get_intersection(ranges, clamp)
        if not ranges:
            continue
        for cuboid in cuboids:
            cuboid.remove_intersection(ranges)
        if on:
            cuboids.append(Cuboid(ranges))
    return sum(cuboid.size() for cuboid in cuboids)


@expect({'test1': 39, 'test2': 590784})
def solve1(instructions):
    return solve(instructions, ((-50, 50), (-50, 50), (-50, 50)))


@expect({'test3': 2758514936282235})
def solve2(instructions):
    return solve(instructions)
