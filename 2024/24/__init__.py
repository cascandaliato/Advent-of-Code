from collections import defaultdict, deque

from pyutils import *


def normalize(op, op1, op2):
    return (op, *sorted([op1, op2]))


def parse(lines):
    wires = {}
    for i, line in enumerate(lines):
        if not line:
            break
        var, val = line.split(": ")
        wires[var] = int(val)

    gates = {}
    for line in lines[i + 1 :]:
        op1, op, op2, out = line.replace(" -> ", " ").split()
        gates[out] = normalize(op, op1, op2)

    return wires, gates


ops = {
    "AND": lambda a, b: a and b,
    "OR": lambda a, b: a or b,
    "XOR": lambda a, b: (a and not b) or (b and not a),
}


@expect({"test1": 4, "test2": 2024})
def solve1(input):
    wires, gates = input

    adj, incoming = defaultdict(set), defaultdict(set)
    for out, (op, op1, op2) in gates.items():
        for operand in (op1, op2):
            adj[operand].add(out)
            if operand not in wires:
                incoming[out].add(operand)

    no_indegrees = deque(
        (*gate, out) for out, gate in gates.items() if not incoming[out]
    )
    while no_indegrees:
        op, op1, op2, out = no_indegrees.popleft()
        wires[out] = int(ops[op](wires[op1], wires[op2]))
        for neighbor in adj[out]:
            incoming[neighbor].remove(out)
            if not incoming[neighbor]:
                no_indegrees.append((*gates[neighbor], neighbor))
    res = [str(wires[z]) for z in sorted(wires, reverse=True) if z.startswith("z")]
    return int("".join(res), 2)


# https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder
def solve2(input):
    _, gates = input

    names = {}
    for out, gate in gates.items():
        names[gate] = out

    adders = [("z00", names[("AND", "x00", "y00")])]

    swapped = set()

    def swap(a, b):
        gates[a], gates[b] = gates[b], gates[a]
        names[gates[a]] = a
        names[gates[b]] = b
        swapped.add(a)
        swapped.add(b)

    i = 1
    while i < 45:
        x = f"x{str(i).zfill(2)}"
        y = f"y{str(i).zfill(2)}"
        z = f"z{str(i).zfill(2)}"
        x_xor_y = names[normalize("XOR", x, y)]

        z_gate = gates[z]
        if z_gate[0] == "XOR" and (
            diff := set([x_xor_y, adders[-1][1]]).symmetric_difference(z_gate[1:])
        ):
            swap(*diff)
            continue
        z_actual = names[normalize("XOR", x_xor_y, adders[-1][1])]
        if z_actual != z:
            swap(z_actual, z)
            continue

        x_and_y = names[normalize("AND", x, y)]
        rhs = names[normalize("AND", adders[-1][1], x_xor_y)]
        c = names[normalize("OR", x_and_y, rhs)]

        adders.append((z, c))
        i += 1

    return ",".join(sorted(swapped))
