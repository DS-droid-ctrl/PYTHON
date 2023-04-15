

# Дан список чисел. Определите, сколько в нем встречается различных чисел
"""
# list = [1, 5, 1, 2, 3, 4, 5, 2]
numbers = [input () for i in range(int(input()))]
# for i in range (6):
    # numbers.append(input()) - добавление чисел в конец списка
print(len(set(numbers)))
"""

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
list_nums = [1, 2, 3, 4, 5]
k = int(input('Введите K: '))
for i in range (k):
    list_nums.insert(0, list_nums.pop(-1)) # list_nums.pop()) без -1 все равно удаляет последний элемент
    i += 1
    print(list_nums)