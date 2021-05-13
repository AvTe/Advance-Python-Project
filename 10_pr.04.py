l = [1, 4, 25, 5, 35, 30, 40, 60, 75, 12, 5, 35]

a = filter(lambda a: a%4==0, l)
print(list(a))
