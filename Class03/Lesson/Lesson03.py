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
"""
def fib(n):
    if n in [1, 2]: # это условие выхода из рекурсии
        return 1
    return fib(n-1) + fib(n-2)

list_1 = [] # создали пустой список, в который будем добавлять результаты выполнения функции fib(i)
for i in range(1, 10):
    list_1.append(fib(i)) # append - функция добавления значений в список list_1
print(list_1)
"""

# Быстрая сортировка
"""
def quicksort(array):
    if len(array) < 2: # это условие выхода из рекурсии (пока в массиве останется 1 элемент)
        return array
    else:
        pivot = array[0] # переменная, в которую поместитили первый элемент массива
        less = [i for i in array[1:] if i <= pivot] # создаем генератор списка, в который записываем значения меньше pivot начиная со второго элемента (array[1:] - срез списка)
        greater = [i for i in array[1:] if i > pivot] # создаем генератор списка, в который записываем значения больше pivot начиная со второго элемента (array[1:] - срез списка)
    return quicksort(less) + [pivot] + quicksort(greater) # возвращаем отсортированный (quicksort) список less + список ([]) pivot + отсортированный (quicksort) список greater
print(quicksort([10, 5, 2, 3])) # [2, 3, 5, 10]
"""
# Быстрая сортировка
# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2, 3]
# ○ pivot = 10
# ○ less = [5, 2, 3]
# ○ greater = []
# ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
# ○ array = [5, 2, 3]
# ○ pivot = 5
# ○ less = [2, 3]
# ○ greater = []
# ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии
# добавляется список [10]
# ● 3-е повторение рекурсии:
# ○ array = [2, 3]
# ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]



