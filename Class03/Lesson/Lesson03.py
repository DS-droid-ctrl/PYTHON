# Функция — это фрагмент программы, используемый многократно

# def function_name(x):
 # body line 1
 # ...
 # body line n
 # optional return

    # Необходимо создать функцию sumNumbers(n), которая будет
    # считать сумму всех элементов от 1 до n.

"""
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1): # range не включает последний элемент поэтому n + 1
        summa += i
    print(summa)
# Для того, чтобы вызвать функцию необходимо написать ее имя и в скобочках передать параметры
sumNumbers(5)
# или возврат функции
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1): # range не включает последний элемент поэтому n + 1
        summa += i
    return summa
print(sumNumbers(5))
"""
# Сколько данных принимается столько и передается
# def sumNumbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1): # range не включает последний элемент поэтому n + 1
#         summa += i
#     return summa
# print(sumNumbers(5, 'qwerty'))

"""
n = int(input())  # 5
sumNumbers(n)
"""
# Неограниченное количество аргументов
"""
def sum_str(*args): # с помощью *args мы можем передавать любые значения входных данных (аргументов)
    res = 0
    for i in args:
        res += '' # строки
    return res
print(sum_str('w', 'e', 'l', 'l'))
print(sum_str('d', 'o', 'u', 'n'))
"""
"""
def sum_str(*args): # с помощью *args мы можем передавать любые значения входных данных (аргументов)
    res = 0
    for i in args:
        res += i # int
    return res
print(sum_str(1, 8, 9))
"""

# Модульность
# Будем импортировать функцию из файла modul.py
"""
import modul
print(modul.max1(5, 9))

# можно програмно сократить название файла
import modul as m
print(m.max1(5, 9))

# или
from modul import max1
print(max1(5, 9))

# Для того чтобы не перечислять все функции, которые мы хотим импортировать из файла modul.py (например from modul import max1, max2 и др)
from modul import * # ставим звездочку и все функции будут импортированы

from modul import f
print(f(2.3))
"""

# Рекурсия — это функция, вызывающая сама себя








