# РЕКУРСИЯ И АЛГОРИТМЫ ПРОДОЛЖЕНИЕ

# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.

# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

# 7
# 3 1 3 4 2 4 12

# 6
# 4 15 43 1 15 1

# list = [input() for i in range(n) if for j in list2]

# n = int(input("Введите размер первого массива: "))
# m = int(input("Введите размер второго массива: "))
# list1 = [input() for i in range(n)]
# list2 = [input() for i in range(m)]
# list3 = [i for i in list1 if i not in list1]

# print(*list1)
# print(*list2)
# print(*list3)

"""
list1 = [input() for i in range(int(input("Введите размер первого массива: ")))]
list2 = [input() for i in range(int(input("Введите размер второго массива: ")))]
list3 = [i for i in list1 if i not in list1]

print(*list1)
print(*list2)
print(*list3)
"""

# list1 = [input(f'{i+1}: ') for i in range(int(input("enter the size of first arrray: ")))]
# list2= [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
# list3= [i for i in list1  if i not in list2]

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном
# массиве определит количество элементов,
# у которых два соседних и, при этом,
# оба соседних элемента меньше данного.

# Сначала вводится число N — количество
# элементов в массиве. Далее записаны N
# чисел — элементы массива.
# Массив состоит из целых чисел.
"""
list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
list_k = [i for i in range(1, len(list_n) - 1) if list_n[i - 1] < list_n[i] > list_n[i + 1]]
print(list_k)
"""

# Дан список чисел. Посчитайте,
# сколько в нем пар элементов,
# равных друг другу.

# Считается, что любые два элемента,
# равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел.
# Все числа списка находятся на разных строках.
"""
list_n = [int(input()) for i in range (int(input('Введите количество элементов списка n: ')))]
count = [list_n[i] for i in range(len(list_n)) for j in range(i + 1, len(list_n)) if list_n[j] == list_n[i]]
print(count, len(count))
"""

# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110

# def mult(num):
#     sum = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0: 
#             sum += i
#     return sum
# number = (int(input('Введите число: ')))
# for i in range(number):
#     j = mult(i)
#     if i < j < number and i == mult(j):
#         print(i, j)

def pair(value):
    # Получаем корень числа, отбрасываем дробную часть
    sq_num = int(value ** 0.5)

    # Выставляем начальное значение в переменной
    # Если переменная sq_num возведённая в квадрат
    # не равна полученному числу, прибавляем 0.
    # Иначе прибавляем это число, т.к. оно тоже множитель
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    # Цикл от 2 др корня числа
    for i in range(2, sq_num):

        # Если полученное число делиться на i без остатка
        if value % i == 0:
            # Складываем в переменную значение i
            # и второй делитель, например
            # value = 10, i = 2, второй делитель 5
            res += i + value // i
    return res


for j in range(10, 300):
    # Первое число, это сумма множителей j
    sum1 = pair(j)

    # Второе число, это сумма множителей sum1
    sum2 = pair(sum1)

    # Если второе число равно j и первое число меньше второго
    # Второе условие защита от дубликатов,
    # записанных наоборот
    if sum2 == j and sum1 < sum2:
        print(j, sum1)