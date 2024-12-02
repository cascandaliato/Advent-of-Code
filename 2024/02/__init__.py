from pyutils import *


def parse(lines):
    return [[int(n) for n in line.split()] for line in lines]


def is_safe(report):
    deltas = [b - a for a, b in zip(report[:-1], report[1:])]
    return (
        min(abs(delta) for delta in deltas) >= 1
        and max(abs(delta) for delta in deltas) <= 3
        and min(deltas) * max(deltas) > 0
    )


@expect({"test": 2})
def solve1(input):
    return len([report for report in input if is_safe(report)])


def is_safe_with_tolerance(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True
    return False


@expect({"test": 4})
def solve2(input):
    return len([report for report in input if is_safe_with_tolerance(report)])
