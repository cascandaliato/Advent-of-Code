from pyutils import *


def parse(lines):
    numbers = [int(line) for line in lines]
    indexes = list(range(len(numbers)))
    return (numbers, indexes)


def decrypt(numbers, indexes):
    for idx in range(len(numbers)):
        current = indexes.index(idx)
        new = (current + numbers[idx]) % (len(numbers) - 1)
        indexes.pop(current)
        indexes.insert(new, idx)


def answer(numbers, indexes):
    zero = indexes.index(numbers.index(0))
    return sum(numbers[indexes[(zero + k) % len(numbers)]] for k in (1000, 2000, 3000))


@expect({'test': 3})
def solve1(data):
    decrypt(*data)
    return answer(*data)


@expect({'test': 1623178306})
def solve2(data):
    numbers, indexes = [n * 811589153 for n in data[0]], data[1]
    for _ in range(10):
        decrypt(numbers, indexes)
    return answer(numbers, indexes)
