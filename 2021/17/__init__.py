import re

from pyutils import *


def parse(lines):
    m = re.search(r'x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', lines[0])
    return tuple(int(n) for n in m.groups())


def solve(x1, x2, y1, y2):
    maxh, count = 0, 0
    for xi in range(x2+1):
        for yi in range(y1, -y1+1):
            cur_pos = (0, 0)
            cur_vel = (xi, yi)
            for _ in range(1000):
                if x1 <= cur_pos[0] <= x2 and y1 <= cur_pos[1] <= y2:
                    maxh, count = max(maxh, yi*(yi+1)//2), count+1
                    break
                if cur_pos[0] > x2 or cur_pos[1] < y1:
                    break
                cur_pos = (cur_pos[0]+cur_vel[0], cur_pos[1]+cur_vel[1])
                cur_vel = (max(cur_vel[0]-1, 0), cur_vel[1]-1)
    return {'maxh': maxh, 'count': count}


@expect({'test': 45})
def solve1(input):
    return solve(*input)['maxh']


@expect({'test': 112})
def solve2(input):
    return solve(*input)['count']
