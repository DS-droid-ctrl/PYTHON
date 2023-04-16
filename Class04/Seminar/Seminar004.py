"""
# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d

# string = "a a a b c a a d c d".split

# for i in range(len(string)):
#     string[i] += f"_{string[0:i-1].count(string[i])}"
# print(*string)

# string = "a a a b c a a d c d"

# dict = {}.fromkeys(string, 0)

# for i in string:
#     if dict[i] != 0:
#         print(f"{i}_{dict[i]}", end=" ")
#     else:
#         print(i, end=" ")
#     dict[i] += 1

string = "a a a b c a a d c d d".split()

dict = {}.fromkeys(string, 0) # .fromkeys собирает значения в словарь с ключом 0

for i in string:
    print(f"{i}_{dict[i]}" if dict[i] else i, end=" ") 
    # end=" " - для вывода на одной строке; dict[i] - вытягивает значение и если 
    # встречается в первый раз, то просто записывается элемент (else i), если уже была, 
    # то выводится количество символов (_1 или _{dict[i]})
    dict[i] += 1
"""

"""
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text = text.lower()
print(len(set(text.split())))


text = input('Введите текст: ').upper() # .upper() можно поставить и сюда
#print(res_text)
print(f'Количество различных слов в тексте: ', len(set(text.split())))
"""

# Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам

# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
#
# print(max_number)

# n = int(input())
# max_number = -1
# while n > 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# 
# print(max_number)