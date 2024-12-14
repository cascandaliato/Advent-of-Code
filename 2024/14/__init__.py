from itertools import count

from pyutils import *

# import png


def parse(lines):
    robots = []
    for line in lines:
        p, v = line.split(" ")
        px, py = p[2:].split(",")
        vx, vy = v[2:].split(",")
        robots.append(((int(px), int(py)), (int(vx), int(vy))))
    return robots


# @expect({"test": 12})
def solve1(input):
    # w, h = 11, 7
    w, h = 101, 103
    q1, q2, q3, q4 = 0, 0, 0, 0
    for (px, py), (vx, vy) in input:
        x = (px + 100 * vx) % w
        y = (py + 100 * vy) % h
        if x < w // 2 and y < h // 2:
            q1 += 1
        elif x > w // 2 and y < h // 2:
            q2 += 1
        elif x < w // 2 and y > h // 2:
            q3 += 1
        elif x > w // 2 and y > h // 2:
            q4 += 1
    return q1 * q2 * q3 * q4


def solve2(input):
    w, h = 101, 103

    # # manual inspection
    # writer = png.Writer(width=w, height=h, bitdepth=1)
    # for i in range(10000):
    #     image = [[0] * w for _ in range(h)]
    #     for (px, py), (vx, vy) in input:
    #         x = (px + i * vx) % w
    #         y = (py + i * vy) % h
    #         image[y][x] = 1
    #     with open(f"{str(i).zfill(5)}.png", "wb") as f:
    #         writer.write(f, image)

    for i in count():
        robots = set()
        for (px, py), (vx, vy) in input:
            x = (px + i * vx) % w
            y = (py + i * vy) % h
            robots.add((x, y))
        if len(robots) == len(input):
            return i
