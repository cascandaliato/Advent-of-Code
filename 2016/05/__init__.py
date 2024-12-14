import hashlib
import itertools

from pyutils import *


def parse(lines):
    return lines[0].encode("utf-8")


@expect({"test": "18f47a30"})
def solve1(input):
    password = ""
    for i in itertools.count():
        hash = hashlib.md5(input + str(i).encode("utf-8")).hexdigest()
        if hash.startswith("00000"):
            password += hash[5]
            if len(password) == 8:
                return password


@expect({"test": "05ace8e3"})
def solve2(input):
    password, length = [None] * 8, 0
    for i in itertools.count():
        hash = hashlib.md5(input + str(i).encode("utf-8")).hexdigest()
        if (
            hash.startswith("00000")
            and hash[5] in "01234567"
            and password[int(hash[5])] is None
        ):
            password[int(hash[5])] = hash[6]
            length += 1
            if length == 8:
                return "".join(password)
