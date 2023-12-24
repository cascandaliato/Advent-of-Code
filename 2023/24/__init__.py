import sympy
from pyutils import *


def parse(lines):
    hailstones = []
    for line in lines:
        xyz, v = line.split(" @ ")
        x0, y0, z0 = map(int, xyz.split(", "))
        vx, vy, vz = map(int, v.split(", "))
        hailstones.append(((x0, y0, z0), (vx, vy, vz)))
    return hailstones


# @expect({"test": 2})
def solve1(hailstones):
    # l, r = 7, 27
    l, r = 200000000000000, 400000000000000
    count = 0
    for i in range(len(hailstones)):
        (xi, yi, _), (vxi, vyi, _) = hailstones[i]
        for j in range(i + 1, len(hailstones)):
            (xj, yj, _), (vxj, vyj, _) = hailstones[j]
            det = +vyi * vxj - vxi * vyj
            if det == 0:
                continue

            ti = (-vyj * (xj - xi) + vxj * (yj - yi)) / det
            tj = (-vyi * (xj - xi) + vxi * (yj - yi)) / det

            if ti < 0 or tj < 0:
                continue

            if all(
                l <= v <= r
                for v in [
                    xi + ti * vxi,
                    yi + ti * vyi,
                    xj + tj * vxj,
                    yj + tj * vyj,
                ]
            ):
                count += 1
    return count


@expect({"test": 47})
def solve2(hailstones):
    (x0, y0, z0), (vx0, vy0, vz0) = hailstones[0]
    (x1, y1, z1), (vx1, vy1, vz1) = hailstones[1]
    (x2, y2, z2), (vx2, vy2, vz2) = hailstones[2]
    x, y, z, vx, vy, vz, t0, t1, t2 = sympy.symbols("x y z vx vy vz t0 t1 t2")
    equations = [
        x + vx * t0 - x0 - vx0 * t0,
        y + vy * t0 - y0 - vy0 * t0,
        z + vz * t0 - z0 - vz0 * t0,
        x + vx * t1 - x1 - vx1 * t1,
        y + vy * t1 - y1 - vy1 * t1,
        z + vz * t1 - z1 - vz1 * t1,
        x + vx * t2 - x2 - vx2 * t2,
        y + vy * t2 - y2 - vy2 * t2,
        z + vz * t2 - z2 - vz2 * t2,
    ]
    solutions = sympy.solve(equations, x, y, z, vx, vy, vz, t0, t1, t2)
    return sum(solutions[0][:3])
