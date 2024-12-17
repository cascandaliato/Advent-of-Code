from pyutils import *


def parse(lines):
    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    program = [int(n) for n in lines[4].split(": ")[1].split(",")]
    return a, b, c, program


def solve(input):
    reg_a, reg_b, reg_c, program = input

    def literal(opd):
        return opd

    def combo(opd):
        match opd:
            case 0 | 1 | 2 | 3:
                return opd
            case 4:
                return reg_a
            case 5:
                return reg_b
            case 6:
                return reg_c
            case 7:
                raise ValueError()

    pointer, output = 0, []
    while pointer < len(program):
        jumped, opd = False, int(program[pointer + 1])
        match program[pointer]:
            case 0:
                reg_a = reg_a // (2 ** combo(opd))
            case 1:
                reg_b ^= literal(opd)
            case 2:
                reg_b = combo(opd) % 8
            case 3:
                if reg_a != 0:
                    pointer = literal(opd)
                    jumped = True
            case 4:
                reg_b ^= reg_c
            case 5:
                output.append(combo(opd) % 8)
            case 6:
                reg_b = reg_a // (2 ** combo(opd))
            case 7:
                reg_c = reg_a // (2 ** combo(opd))

        if not jumped:
            pointer += 2
    return output


@expect({"test1": "4,6,3,5,6,3,5,2,1,0"})
def solve1(input):
    return ",".join(str(n) for n in solve(input))


@expect({"test2": 117440})
def solve2(input):
    _, reg_b, reg_c, program = input

    digits = []

    def digits_to_n():
        return sum(m[-1] * 8 ** (len(digits) - i - 1) for i, m in enumerate(digits))

    while len(digits) < len(program):
        candidates = []
        for reg_a in range(8):
            output = solve((reg_a + digits_to_n() * 8, reg_b, reg_c, program))
            if output[0] == program[-1 - len(digits)]:
                candidates.append(reg_a)
        if candidates:
            digits.append(list(reversed(candidates)))
        else:
            digits[-1].pop()

        while not digits[-1]:
            digits.pop()
            digits[-1].pop()

    return digits_to_n()
