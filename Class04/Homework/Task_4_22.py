# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств

from random import randint
n = int(input('Введите количество элементов в массиве A: '))
a = [randint(1, 10) for _ in range(n)]
m = int(input('Введите количество элементов в массиве B: '))
b = [randint(1, 10) for _ in range(m)]
print(*a)
print(*b)
for i in range(m):
    a.append(b[i])
    i += 1
a.sort()
c = set(a)
print(*c)
