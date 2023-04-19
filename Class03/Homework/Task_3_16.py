# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

"""
from random import randint
N = int(input('Введите количество элементов в массиве: '))
A = [randint(1, N) for _ in range(N)]
X = int(input('Введите искомое число: '))
print(N)
print(*A)
print(X)
count = 0
for i in range(N):
    if X == A[i]:
        count += 1
    i += 1
print(count)
"""

from random import randint
N = int(input('Введите количество элементов в массиве: '))
A = [randint(1, N) for _ in range(N)]
X = int(input('Введите искомое число: '))
print(N)
print(*A)
print(X)
count = A.count(X)
print(count)
