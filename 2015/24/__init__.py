from math import inf
from pyutils import *


def parse(lines):
    lines.reverse()
    return [int(line) for line in lines]


def solve(nums, target):
    shortest, lowest_entanglement = inf, inf

    def gen(target=target, length=0, entanglement=1, i=0):
        nonlocal shortest, lowest_entanglement

        if target == 0:
            if length < shortest or (
                length == shortest and entanglement < lowest_entanglement
            ):
                shortest = length
                lowest_entanglement = entanglement
                yield tuple()
        elif target > 0 and length < shortest and i < len(nums):
            for t in gen(target - nums[i], length + 1, entanglement * nums[i], i + 1):
                yield (nums[i],) + t
            yield from gen(target, length, entanglement, i + 1)

    entanglement = 1
    for n in list(gen())[-1]:
        entanglement *= n
    return entanglement


@expect({"test": 99})
def solve1(nums):
    return solve(nums, sum(nums) // 3)


@expect({"test": 44})
def solve2(nums):
    return solve(nums, sum(nums) // 4)
