import re

from collections import deque

from pyutils import *


def parse(lines):
    valves = {}
    for line in lines:
        m = re.search(
            "Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", line
        )
        valves[m.group(1)] = {"rate": int(m.group(2)),
                              "next": set(m.group(3).split(", "))}

    def distance(frm, to):
        q, visited = deque([(0, frm)]), set()
        while q:
            cost, current = q.pop()
            if current == to:
                return cost
            if current in visited:
                continue
            visited.add(current)
            for valve_next in valves[current]["next"]:
                q.appendleft((cost + 1, valve_next))

    good_valves = [valve for valve in valves if valves[valve]["rate"] > 0]

    return {
        valve: {
            'rate': valves[valve]['rate'],
            'to': {other: distance(valve, other) for other in good_valves if other != valve}
        } for valve in good_valves + ["AA"]
    }


@expect({'test': 1651})
def solve1(valves):
    def solve(current, opened, remaining_time):
        results, total_rate = [], sum(valves[valve]["rate"]
                                      for valve in opened)

        for valve, distance in valves[current]['to'].items():
            if valve in opened or distance + 1 >= remaining_time:
                continue
            results.append(
                (distance + 1) * total_rate
                + solve(
                    valve,
                    opened + (valve,),
                    remaining_time - distance - 1,
                )
            )

        return max(results) if results else remaining_time * total_rate

    return solve("AA", tuple(), 30)


@expect({'test': 1707})
def solve2(valves):
    def it(sequence, remaining_time):
        current = sequence[-1]
        for valve in valves[current]['to']:
            distance = valves[current]['to'][valve]
            if distance+1 < remaining_time and valve not in sequence:
                yield from it(sequence + (valve,), remaining_time - distance - 1)
        yield sequence

    def total_pressure(sequence, remaining_time):
        pressure, rate = 0, 0
        for idx, valve in enumerate(sequence[1:]):
            distance = valves[sequence[idx]]['to'][valve]
            remaining_time -= distance + 1
            pressure += rate * (distance + 1)
            rate += valves[valve]["rate"]
        pressure += remaining_time * rate
        return pressure

    paths = []
    for sequence in it(("AA",), 26):
        paths.append((total_pressure(sequence, 26), sequence))
    paths.sort(reverse=True)

    best = 0
    for idx, path1 in enumerate(paths):
        for path2 in paths[idx + 1:]:
            if path2[0] < best - path1[0]:
                break
            if any(v in path1[1][1:] for v in path2[1][1:]):
                continue
            best = max(best, path1[0] + path2[0])
    return best
