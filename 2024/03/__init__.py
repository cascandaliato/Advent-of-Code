import operator
import re

from pyutils import *

mul = operator.mul
mul_re = r"mul\([1-9][0-9]{,2},[1-9][0-9]{,2}\)"


def parse(lines):
    return lines


@expect({"test1": 161})
def solve1(input):
    return sum(eval(m) for line in input for m in re.findall(mul_re, line))


@expect({"test2": 48})
def solve2(input):
    instructions = [
        op
        for line in input
        for op in re.findall(rf"(?:{mul_re}|do\(\)|don\'t\(\))", line)
    ]

    res, enabled = 0, True
    for instruction in instructions:
        match instruction:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case m:
                if enabled:
                    res += eval(m)
    return res
