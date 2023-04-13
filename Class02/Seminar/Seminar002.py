"""
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

n = int(input('Введите значение числа N: '))
fact = n
while n > 1:
    fact = fact * (n-1)
    n -= 1
print(fact)

# num = int(input("Введите число: "))+1
# flag = 1
# if num<0:
#     print("Введите положительное число")
# else:
#     if num == 1:
#         print("1")
#     else:
#         while num != 1:
#             flag *= num - 1
#             num-=1
# print(flag)

"""
"""
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1

# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = int(input())
a1 = 0
a2 = 1
i = 2

while a2 <= n:
    if a2 == n:
        print(i)
        break
    a1, a2 = a2, a1 + a2
    i += 1
else:
    print(-1)


# n = int(input())
# a1 = 0
# a2 = 1
# i = 2

# while a2 <= n:
#     if a2 == n:
#         print(i)
#         break
#     a1, a2 = a2, a1 + a2
#     i += 1
#     if a2 > n:
#         print(-1)
#         break
"""
"""
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

n = int(input("Введите число: "))

count = 0
result = 0

for i in range(n) :

    temp = int(input(f"{i + 1}-день: "))

    if(temp > 0) :

        count = count + 1
        
        if(count > result) :
            result = count

    else :
        count = 0

print(f"Количество дней с средней температурой больше 0 градусов: {result}")
"""

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# n = int(input())

# weight = int(input())
# max_weight = weight
# min_weight = weight

# for _ in range(n-1):
#     weight = int(input())
#     if max_weight < weight:
#         max_weight = weight
#     elif min_weight > weight:
#         min_weight = weight

# print(f"{min_weight} {max_weight}")

num = int(input("Введите число: "))
max = 0
min = 100
for i in range(num):
    count = int(input(f"{i+1} - арбуз: "))
    if count>max:
        max = count
    if count<min:
          min = count
print(f"Max: {max}, Min: {min}")
