import os
import requests

from dotenv import load_dotenv
from functools import wraps

requests.packages.urllib3.disable_warnings()


def input(filename='input.txt'):
    return open(filename).read().splitlines()


def download(year, day):
    load_dotenv()
    AOC_SESSION = os.getenv('AOC_SESSION')
    if os.path.exists('input.txt') or not AOC_SESSION:
        return
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    req = requests.get(url, verify=False, cookies={
        'session': AOC_SESSION})
    with open('input.txt', 'x') as f:
        f.write(req.content.decode('utf-8'))


def ints(lines):
    return (int(line) for line in lines)


def expect(expectations):
    def decorator(func):
        func.expectations = expectations
        return func
    return decorator


def tokens(lines, *, sep=' ', map=lambda x: x):
    return (map(line.split(sep)) for line in lines)
