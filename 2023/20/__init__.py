import math
from collections import defaultdict
from pyutils import *

HIGH, LOW = True, False


def broadcast(_, pulse, __, ___):
    return pulse


def flipflop(_, pulse, state, __):
    if pulse == HIGH:
        return None

    state["on"] = not state["on"]
    return state["on"]


def conjunction(source, pulse, state, inputs):
    state[source] = pulse

    return LOW if all(state.get(input, LOW) == HIGH for input in inputs) else HIGH


def noop(_, __, ___, ____):
    return None


def parse(lines):
    modules = defaultdict(lambda: defaultdict(list))
    for line in lines:
        name, destinations = line.split(" -> ")
        if name == "broadcaster":
            modules[name]["state"] = None
            modules[name]["op"] = broadcast
        else:
            t, name = name[0], name[1:]
            match t:
                case "%":
                    modules[name]["state"] = {"on": False}
                    modules[name]["op"] = flipflop
                case _:
                    modules[name]["state"] = defaultdict()
                    modules[name]["op"] = conjunction
        for destination in destinations.split(", "):
            modules[name]["outputs"].append(destination)
            modules[destination]["inputs"].append(name)
    return modules


@expect({"test1": 32000000, "test2": 11687500})
def solve1(modules):
    count = {HIGH: 0, LOW: 0}
    for _ in range(1000):
        q = [("button", "broadcaster", LOW)]
        while q:
            source, destination, pulse = q.pop(0)
            count[pulse] += 1
            m = modules[destination]
            new_pulse = m.get("op", noop)(source, pulse, m["state"], m["inputs"])
            if new_pulse is not None:
                q.extend((destination, output, new_pulse) for output in m["outputs"])
    return count[HIGH] * count[LOW]


def solve2(modules):
    parent = modules["rx"]["inputs"][0]
    grandparents = {m: None for m in modules[parent]["inputs"]}
    button = 0
    while True:
        button += 1
        q = [("button", "broadcaster", False)]
        while q:
            source, destination, pulse = q.pop(0)
            if destination == parent and pulse:
                grandparents[source] = button
                if all(grandparents.values()):
                    return math.lcm(*grandparents.values())
            m = modules[destination]
            new_pulse = m.get("op", noop)(source, pulse, m["state"], m["inputs"])
            if new_pulse is not None:
                q.extend((destination, output, new_pulse) for output in m["outputs"])
