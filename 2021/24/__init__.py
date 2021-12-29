from pyutils import *


def parse(lines):
    alu = [line.split() for line in lines]
    alu = list(t[1] for t in filter(lambda t: any(t[0] %
                                    18 == d for d in [4, 5, 15]), enumerate(alu)))
    return [alu[i:i+3] for i in range(0, len(alu)-2, 3)]


def solve(triplets, maximize=True):
    coeffs, model = [], [0]*14
    for i, triplet in enumerate(triplets):
        (_, _, div), (_, _, offset), (_, _, c) = triplet
        if int(div) == 1:
            coeffs.append((int(c), i))
        else:
            coeff, j = coeffs.pop()
            coeffs.insert(0, (coeff+int(offset), j, i))
    for c, i, j in coeffs:
        model[i] = min(9, 9-c) if maximize else max(1, 1-c)
        model[j] = c+model[i]
    return ''.join(str(d) for d in model)


def solve1(triplets):
    return solve(triplets)


def solve2(triplets):
    return solve(triplets, maximize=False)
