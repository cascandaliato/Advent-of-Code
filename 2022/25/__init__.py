from pyutils import *


def parse(lines):
    return lines


@expect({'test': '2=-1=0'})
def solve1(lines):
    def to_int(snafu):
        n = 0
        for i, d in enumerate(reversed(snafu)):
            n += (int(d) if d.isnumeric() else {'-': -1, '=': -2}[d])*5**i
        return n

    def to_snafu(n):
        snafu = []
        while n != 0:
            r = n % 5
            n -= r
            if r > 2:
                n += 5
                r = {3: '=', 4: '-'}[r]
            n //= 5
            snafu.append(str(r))
        return ''.join(reversed(snafu))

    return to_snafu(sum(to_int(line) for line in lines))


@expect({'test': 2})
def solve2(input):
    return None
