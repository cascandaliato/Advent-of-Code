from functools import cache
from operator import add, mul

from pyutils import *


def parse(lines):
    equations = []
    for line in lines:
        total, operands = line.split(": ")
        equations.append((int(total), tuple(int(n) for n in operands.split())))
    return equations


def with_operators(ops):
    @cache
    def dp(equation, i, total):
        if i == len(equation[1]):
            return total == equation[0]
        if total > equation[0]:
            return False
        # return any(dp(equation, i + 1, op(total, equation[1][i])) for op in ops)
        for op in ops:
            if dp(equation, i + 1, op(total, equation[1][i])):
                return True
        return False

    return dp


@expect({"test": 3749})
def solve1(equations, operators=[add, mul]):
    dp = with_operators(operators)
    return sum(equation[0] for equation in equations if dp(equation, 1, equation[1][0]))


@expect({"test": 11387})
def solve2(equations):
    return solve1(equations, operators=[add, mul, lambda a, b: int(str(a) + str(b))])
