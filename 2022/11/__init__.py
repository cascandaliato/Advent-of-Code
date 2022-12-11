import math

from dataclasses import dataclass, field
from typing import Any

from pyutils import *


@dataclass
class Monkey:
    items: Any
    operation: Any
    divisible_by: Any
    if_true: Any
    if_false: Any


def parse(lines):
    monkeys = []
    it = iter(lines)
    try:
        while True:
            next(it)
            items = ints(next(it).replace(
                "  Starting items: ", "").split(", "))
            operation = eval('lambda old: ' +
                             str(next(it).replace("  Operation: new = ", "")))
            divisible_by = int(next(it).replace("  Test: divisible by ", ""))
            if_true = int(next(it).replace(
                "    If true: throw to monkey ", ""))
            if_false = int(next(it).replace(
                "    If false: throw to monkey ", ""))
            monkeys.append(
                Monkey(items, operation, divisible_by, if_true, if_false))
            next(it)
    except StopIteration:
        pass
    return monkeys


def solve(monkeys, rounds, manage_worriedness):
    no_inspected = [0]*len(monkeys)
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            for old in monkey.items:
                no_inspected[i] += 1
                item = manage_worriedness(monkey.operation(old))
                if item % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(item)
                else:
                    monkeys[monkey.if_false].items.append(item)
            monkey.items = []
    most_active = list(sorted(no_inspected, reverse=True))
    return most_active[0]*most_active[1]


@expect({'test': 10605})
def solve1(monkeys):
    return solve(monkeys, rounds=20, manage_worriedness=lambda w: w//3)


@expect({'test': 2713310158})
def solve2(monkeys):
    lcm = math.prod(monkey.divisible_by for monkey in monkeys)
    return solve(monkeys, rounds=10000, manage_worriedness=lambda w: w % lcm)
