import os
import requests

from dotenv import load_dotenv
from itertools import product, tee

requests.packages.urllib3.disable_warnings()


def puzzle_input(filename='input.txt'):
    return open(filename).read().splitlines()


def download(year, day):
    load_dotenv(override=True)
    AOC_SESSION = os.getenv('AOC_SESSION')
    if os.path.exists('input.txt') or not AOC_SESSION:
        return
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = requests.get(url, verify=False, cookies={
        'session': AOC_SESSION})
    with open('input.txt', 'x') as f:
        f.write(req.content.decode('utf-8'))


def ints(nums):
    return list(int(num) for num in nums)


def expect(expectations):
    def decorator(func):
        func.expectations = expectations
        return func
    return decorator


def tokens(lines, *, sep=' ', map=lambda x: x):
    return (map(line.split(sep)) for line in lines)


def split_by_empty_line(lines):
    ans = [[]]
    for line in lines:
        if line:
            ans[-1].append(line)
        else:
            ans.append([])
    return ans


def findindex(p, l):
    return next(filter(lambda t: p(t[0], t[1]), enumerate(l)), (-1, None))[0]


def pairwise(iterable):
    """Polyfill for Python 3.8 (https://docs.python.org/3.8/library/itertools.html)."""
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def sparse(image, char='#'):
    return set((c, r) for r, c in product(range(len(image)), repeat=2) if image[r][c] == char)
