from pyutils import *

PREV, NEXT = 1, 2


def parse(lines):
    numbers, zero = [], None
    for line in lines:
        n = [int(line), None, None]
        if numbers:
            n[PREV] = numbers[-1]
            numbers[-1][NEXT] = n
        numbers.append(n)
        if n[0] == 0:
            zero = n
    numbers[-1][NEXT] = numbers[0]
    numbers[0][PREV] = numbers[-1]
    return numbers, zero


def get_nth(zero, n):
    nth = zero
    for _ in range(n):
        nth = nth[NEXT]
    return nth[0]


def decrypt(numbers):
    for i, n in enumerate(numbers):
        for _ in range(n[0] % (len(numbers)-1)):
            old_prev = n[PREV]
            old_next = n[NEXT]
            old_next_next = old_next[NEXT]

            old_prev[NEXT] = old_next
            old_next[PREV] = old_prev
            old_next[NEXT] = n
            old_next_next[PREV] = n

            n[PREV] = old_next
            n[NEXT] = old_next_next


def answer(numbers, zero):
    pos1, pos2, pos3 = 1000 % len(numbers), 2000 % len(
        numbers), 3000 % len(numbers)
    return get_nth(zero, pos1)+get_nth(zero, pos2)+get_nth(zero, pos3)


@expect({'test': 3})
def solve1(data):
    numbers, zero = data
    decrypt(numbers)
    return answer(numbers, zero)


@expect({'test': 1623178306})
def solve2(data):
    numbers, zero = data
    for n in numbers:
        n[0] *= 811589153
    for _ in range(10):
        decrypt(numbers)
    return answer(numbers, zero)
