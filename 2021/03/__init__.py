from pyutils import *


def to_int(tuple):
    return int(''.join(str(digit) for digit in tuple), 2)


@expect({'test': 198})
def solve1(lines):
    ones = tuple(sum(int(line[i]) for line in lines)
                 for i in range(len(lines[0])))
    gamma_rate = tuple(int(ones[i] >= len(lines)/2)
                       for i in range(len(lines[0])))
    epsilon_rate = tuple(-d+1 for d in gamma_rate)
    return to_int(gamma_rate)*to_int(epsilon_rate)


def sieve(lines, selector):
    for i in range(len(lines[0])):
        if len(lines) == 1:
            break
        by_ith_digit = {d: [line for line in lines if int(line[i]) == d]
                        for d in [0, 1]}
        lines = by_ith_digit[selector(by_ith_digit)]
    return to_int(lines[0])


@ expect({'test': 230})
def solve2(input):
    def most_common(by_ith_digit):
        return 1 if len(by_ith_digit[1]) >= len(by_ith_digit[0]) else 0

    def least_common(d):
        return -most_common(d)+1

    oxygen_generator_rating = sieve(input, most_common)
    co2_scrubber_rating = sieve(input, least_common)

    return oxygen_generator_rating*co2_scrubber_rating
