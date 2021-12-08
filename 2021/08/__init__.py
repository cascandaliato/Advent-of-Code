from pyutils import *


def parse(lines):
    return [tuple([set(p) for p in s.split()] for s in line.split(' | ')) for line in lines]


@expect({'test1': 26})
def solve1(input):
    return len([s for entry in input for s in entry[1] if len(s) in [2, 3, 4, 7]])


easy_criteria = [
    (lambda p, _: len(p) == 2, 1),
    (lambda p, _: len(p) == 3, 7),
    (lambda p, _: len(p) == 4, 4),
    (lambda p, _: len(p) == 7, 8),
]

hard_criteria = [
    (lambda p, segs: len(p) == 6 and p.intersection(segs[4]) == segs[4], 9),
    (lambda p, segs: len(p) == 6 and p.intersection(segs[1]) == segs[1], 0),
    (lambda p,    _: len(p) == 6,                                        6),
    (lambda p, segs: len(p) == 5 and p.intersection(segs[1]) == segs[1], 3),
    (lambda p, segs: len(p) == 5 and len(p.intersection(segs[4])) == 2,  2),
    (lambda p,    _: len(p) == 5,                                        5)
]


def identify(patterns, criteria, segments):
    for pattern in patterns:
        for predicate, digit in criteria:
            if predicate(pattern, segments):
                segments[digit] = pattern
                break


def pattern_to_digit(pattern, segments):
    return next(filter(lambda criteria: criteria[0](pattern, segments),
                       easy_criteria + hard_criteria))[1]


@expect({'test1': 61229, 'test2': 5353})
def solve2(input):
    total = 0
    for patterns, output in input:
        segments, output_int = {}, 0
        identify(patterns, easy_criteria, segments)  # 1, 4, 7, 8
        for pattern in output:
            output_int = output_int*10 + pattern_to_digit(pattern, segments)
        total += output_int
    return total
