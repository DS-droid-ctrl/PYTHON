# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
n = int(input('Введите количество элементов в массиве: '))
list_1 = [randint(-10, 20) for _ in range(n)]
print(list_1)
list_2 = []
for i in range(len(list_1)):
    if 5 < list_1[i] < 15:
        list_2.append(i)
print(list_2)