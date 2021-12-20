from collections import Counter

from pyutils import *


def parse(lines):
    template, rules = split_by_empty_line(lines)
    return Counter(list(pairwise(template[0])) + [(template[0][-1], 0)]), {tuple(k): v for k, v in [rule.split(' -> ') for rule in rules]}


def step(template, rules):
    delta = Counter()
    for pair in template.keys():
        if pair[1] == 0:
            continue
        delta[pair] -= template[pair]
        delta[(pair[0], rules[pair])] += template[pair]
        delta[(rules[pair], pair[1])] += template[pair]
    template.update(delta)


def run_steps_and_count(n, template, rules):
    for _ in range(n):
        step(template, rules)
    count = Counter({char: sum(template[k] for k in template.keys(
    ) if k[0] == char) for char in set(c for c, _ in template.keys())})
    return count.most_common(1)[0][1] - count.most_common()[-1][1]


@expect({'test': 1588})
def solve1(input):
    return run_steps_and_count(10, input[0], input[1])


@expect({'test': 2188189693529})
def solve2(input):
    return run_steps_and_count(40, input[0], input[1])
