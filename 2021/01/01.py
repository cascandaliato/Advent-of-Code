input = [int(l.rstrip()) for l in open('input.txt').readlines()]

print('Part 1:', sum(int(a > b) for a, b in zip(input[1:], input[:-1])))

print('Part 2:', sum(int(a > b) for a, b in zip(input[3:], input[:-3])))
