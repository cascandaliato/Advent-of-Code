from pyutils import *


def parse(lines):
    sep = lines.index("")
    workflows = {}
    for w in lines[:sep]:
        name, rest = w.split("{")
        conditions = rest[:-1].split(",")
        for i in range(len(conditions) - 1):
            condition, target = conditions[i].split(":")
            conditions[i] = [
                condition[:1],
                condition[1:2],
                int(condition[2:]),
                target,
            ]
        workflows[name] = conditions

    parts = []
    for p in lines[sep + 1 :]:
        parts.append(
            {attr.split("=")[0]: int(attr.split("=")[1]) for attr in p[1:-1].split(",")}
        )

    return workflows, parts


@expect({"test": 19114})
def solve1(data):
    def next_(workflow, part):
        for k, op, n, target in workflow[:-1]:
            if (op == ">" and part[k] > n) or (op == "<" and part[k] < n):
                return target
        return workflow[-1]

    workflows, parts = data
    accepted = 0
    for part in parts:
        w = "in"
        while True:
            if w == "A":
                accepted += sum(part.values())
                break
            elif w == "R":
                break
            else:
                w = next_(workflows[w], part)
    return accepted


@expect({"test": 167409079868000})
def solve2(data):
    def intersect(ranges, condition):
        k, op, n = condition

        l, r = ranges[k].start, ranges[k].stop
        intersection = ranges.copy()
        rest = ranges.copy()

        if op == "<":
            intersection[k] = range(l, min(r, n))
            rest[k] = range(min(r, n), r)
        else:
            intersection[k] = range(max(l, n + 1), r)
            rest[k] = range(l, max(l, n + 1))

        return intersection, rest

    workflows, _ = data
    q, accepted = [("in", {k: range(1, 4001) for k in "xmas"})], 0
    while q:
        w, ranges = q.pop()
        if w == "A":
            sub = 1
            for r in ranges.values():
                sub *= len(r)
            accepted += sub
            continue
        elif w == "R":
            continue
        else:
            workflow = workflows[w]
            for *condition, target in workflow[:-1]:
                good, rest = intersect(ranges, condition)
                q.append((target, good))
                ranges = rest
            q.append((workflow[-1], ranges))
    return accepted
