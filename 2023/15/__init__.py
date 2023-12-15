from pyutils import *


def parse(lines):
    return lines[0].split(",")


def aoc_hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h


@expect({"test": 1320})
def solve1(initseq):
    return sum(aoc_hash(s) for s in initseq)


@expect({"test": 145})
def solve2(initseq):
    initseq = [
        (s[:-1], "-", None)
        if s.endswith("-")
        else (s.split("=")[0], "=", int(s.split("=")[1]))
        for s in initseq
    ]

    boxes = [dict() for _ in range(256)]
    for label, op, n in initseq:
        match op:
            case "-":
                boxes[aoc_hash(label)].pop(label, None)
            case "=":
                boxes[aoc_hash(label)][label] = n

    power = 0
    for box in range(256):
        for slot, (_, focal_len) in enumerate(boxes[box].items()):
            power += (box + 1) * (slot + 1) * focal_len
    return power
