from pyutils import *


def parse(lines):
    return set([tuple(int(n) for n in line.split(',')) for line in lines])


deltas = [(-1, 0, 0), (+1, 0, 0), (0, -1, 0),
          (0, +1, 0), (0, 0, -1), (0, 0, +1)]


@expect({'test': 64})
def solve1(cubes):
    count = 0
    for x, y, z in cubes:
        for dx, dy, dz in deltas:
            if (x+dx, y+dy, z+dz) not in cubes:
                count += 1
    return count


@expect({'test': 58})
def solve2(cubes):
    x_min, x_max = min(x for x, _, _ in cubes), max(x for x, _, _ in cubes)
    range_x = range(x_min-1, x_max+2, 1)

    y_min, y_max = min(y for _, y, _ in cubes), max(y for _, y, _ in cubes)
    range_y = range(y_min-1, y_max+2, 1)

    z_min, z_max = min(z for _, _, z in cubes), max(z for _, _, z in cubes)
    range_z = range(z_min-1, z_max+2, 1)

    q, visited, surface = [(x_max+1, y_max+1, z_max+1)], set(), set()
    while q:
        x, y, z = q.pop()
        if (x, y, z) in visited or (x, y, z) in cubes or x not in range_x or y not in range_y or z not in range_z:
            continue
        visited.add((x, y, z))
        for dx, dy, dz in deltas:
            q.append((x+dx, y+dy, z+dz))
            if (x+dx, y+dy, z+dz) in cubes:
                surface.add((x, y, z))

    count = 0
    for x, y, z in cubes:
        for dx, dy, dz in deltas:
            if (x+dx, y+dy, z+dz) not in cubes and (x+dx, y+dy, z+dz) in surface:
                count += 1
    return count
