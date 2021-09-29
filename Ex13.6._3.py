# объявление функции
# Корни уравнения

from math import *

def solve(a, b, c):
    d = b * b - (4 * a * c)
    if d == 0:
        x1 = -b / (2 * a)
        x2 = x1
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
    return x1, x2

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(min(x1,x2), max(x1,x2))
