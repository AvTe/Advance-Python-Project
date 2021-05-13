from functools import reduce

l = [3, 8, 455, 3, 5, 45]

a = reduce(max, l)
print(a)