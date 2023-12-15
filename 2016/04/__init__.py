import re
from collections import Counter
from pyutils import *


def parse(lines):
    return [re.search(r"(.*?)(\d+)\[(.*)\]", line).groups() for line in lines]


def is_real(room, checksum):
    return (
        checksum
        == "".join(
            l
            for l, _ in sorted(
                Counter(room.replace("-", "")).most_common(),
                key=lambda t: (-t[1], t[0]),
            )
        )[:5]
    )


@expect({"test": 1514})
def solve1(rooms):
    return sum(int(id) for room, id, checksum in rooms if is_real(room, checksum))


def solve2(rooms):
    for room, id, checksum in rooms:
        if is_real(room, checksum):
            decrypted = []
            for l in room:
                if l == "-":
                    decrypted.append(" ")
                else:
                    decrypted.append(
                        chr(ord("a") + +(ord(l) - ord("a") + int(id)) % 26)
                    )
            if "north" in "".join(decrypted):
                return id
