import math as m
a, b, c = [int(i) for i in input().split(' ')]
print(a, b, c)
tmp = (b**2 + c**2 - a**2)
print(tmp)
print(tmp/(2*b*c))