# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

text = input("Введите рифму:")

import re 

def proverka(text):
    if re.search('[A-Za-z0-9]', text):
        print("Введен некорректный текст")

print(proverka(text))

text = text.split()
print(text)
s4 = 'аеёиоуыэюя'

def extractDigits(text):
    return list(map(lambda el:[el], text))
st = extractDigits(text)
print(st)

list_1 = st[0]
list_2 = st[1]
list_3 = st[2]
print(list_1, list_2, list_3)

str_1 = ' '.join(list_1)
str_2 = ' '.join(list_2)
str_3 = ' '.join(list_3)
print(str_1, str_2, str_3)

s1="".join(c for c in str_1 if c.isalpha())
s2="".join(c for c in str_2 if c.isalpha())
s3="".join(c for c in str_3 if c.isalpha())
print (s1, s2, s3)
print(s4)

def count(s, s4):
    results = 0
    for w in s:
        results += s4.count(w)
    return results
a = count(s1 , s4)
b = count(s2 , s4)
c = count(s3 , s4)
print(a, b, c)

if a == b == c and a != 0 and b != 0 and c != 0:
    print('Парам пам-пам')
else:
    print('Пам парам')

