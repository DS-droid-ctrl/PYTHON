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
    return summa


n = int(input())  # 5
sumNumbers(n)
"""

# Модульность
