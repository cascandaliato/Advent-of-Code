from pyutils import *


def parse(lines):
    def range_(a, b):
        step = 1 if b >= a else -1
        return range(a, b + step, step)

    bricks = []
    for line in lines:
        start, end = line.split("~")
        x1, y1, z1 = map(int, start.split(","))
        x2, y2, z2 = map(int, end.split(","))
        brick = []
        for x in range_(x1, x2):
            for y in range_(y1, y2):
                for z in range_(z1, z2):
                    brick.append([x, y, z])
        bricks.append(brick)
    return bricks


def solve(bricks):
    # fall
    bricks.sort(key=lambda b: min(z for _, _, z in b))
    for i, brick in enumerate(bricks):
        delta_z = min(z for _, _, z in brick) - 1
        for j in range(i):
            for x, y, z in brick:
                for xo, yo, zo in bricks[j]:
                    if x == xo and y == yo:
                        delta_z = min(delta_z, z - zo - 1)
        for b in brick:
            b[2] -= delta_z

    cubes = dict()
    for i, brick in enumerate(bricks):
        for x, y, z in brick:
            cubes[(x, y, z)] = i

    supported = [set() for _ in range(len(bricks))]
    supporters = [set() for _ in range(len(bricks))]
    for i, brick in enumerate(bricks):
        for x, y, z in brick:
            if z > 1 and 0 <= (j := cubes.get((x, y, z - 1), -1)) != i:
                supported[i].add(j)
                supporters[j].add(i)

    not_safe = set(next(iter(s)) for s in supported if len(s) == 1)

    return not_safe, supported, supporters


@expect({"test": 5})
def solve1(bricks):
    not_safe, _, _ = solve(bricks)
    return len(bricks) - len(not_safe)


@expect({"test": 7})
def solve2(bricks):
    not_safe, supported, supporters = solve(bricks)
    ans = 0
    for i in not_safe:
        q, fallen = [i], set()
        while q:
            i = q.pop()
            fallen.add(i)
            for j in supporters[i]:
                if supported[j].issubset(fallen):  # j has no more support
                    q.append(j)
        ans += len(fallen) - 1  # fallen includes the brick being removed
    return ans
