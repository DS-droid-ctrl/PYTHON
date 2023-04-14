# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

n = int(input('Введите число N: '))
pow = 1
for a in range(n):
    if pow <= n - pow:
        pow = pow * 2
        a += 1
        print(pow)
