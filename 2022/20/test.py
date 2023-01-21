numbers = [int(x) * 811589153 for x in open('input.txt')]
indices = list(range(len(numbers)))

# for i in indices * 10:
#     indices.pop(j := indices.index(i))
#     indices.insert((j+numbers[i]) % len(indices), i)

# zero = indices.index(numbers.index(0))
# print(sum(numbers[indices[(zero+p) % len(numbers)]]
#       for p in [1000, 2000, 3000]))

idx = [1, 2, 3]
for i in idx*3:
    print(i)
    idx[0] =42
