# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def sum(a, b):
    if b == 0:
        return a
    
    return sum(a, b - 1) + 1
    
print (sum(a, b))