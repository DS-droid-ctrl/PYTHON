# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
# члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
c = int(input("Введите количество элементов: "))

list = [a]
for i in range(2, c+1):
    a = list[0] + (i - 1) * d
    list.append(a)
print(*list)