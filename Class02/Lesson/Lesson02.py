# СПИСКИ
"""
list_1 = [] # пустой список
list_1 = list()
list_1 = [1, 2, 3, 8]
print(list_1)
print(*list_1) # печатает список без квадратных скобочек и запятых

for i in list_1:
    print(i) # выводит список из цикла
print(len(list_1)) # считает количество элементов в списке

print(list_1[0]) # обращаемся к первому элементу (1)
print(list_1[-1]) # индексация с конца (8)
"""

# ДОБАВЛЕНИЕ ЗНАЧЕНИЙ В СПИСОК

# list_1 = [1, 5]
# print(*list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# УДАЛЕНИЕ ПОСЛЕДНЕГО ЭЛЕМЕНТА
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]
"""

# УДАЛЕНИЕ КОНКРЕТНОГО ЭЛЕМЕНТА ИЗ СПИСКА
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]
"""

# ДОБАВЛЕНИЕ ЭЛЕМЕНТА НА НУЖНУЮ ПОЗИЦИЮ
"""
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11)) # (позиция, значение)
print(list_1) # [12, 7, 11, -1, 21, 0]
"""
# СРЕЗ СПИСКА
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[len(list_1)-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) #[9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]
"""

# Кортеж — это неизменяемый список.
"""
Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты
каких-либо данных от изменений (намеренных или случайных). Кортеж занимает
меньше места в памяти и работают быстрее, по сравнению со списками

t = ()  # создание пустого кортежа
print(type(t))  # class <'tuple'>
t = (1,)
print(type(t)) # class <'int'>
t = (1)
print(type(t))
t = (28, 9, 1990)
print(type(t))
colors = ['red', 'green', 'blue']
print(colors)  # ['red', 'green', 'blue']
print(type(colors)) # <class 'list'>
t = tuple(colors) # преобразование в картеж colors
print(type(t)) # class <'tuple'>
print(t)  # ('red', 'green', 'blue')
t = tuple(['red', 'green', 'blue'])
print(t[0])  # red
print(t[2])  # blue
for e in t:
    print(e)  # red green blue
# TypeError: 'tuple' object does not support(нельзя изменять кортеж)
t[0] = 'black'

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v
print(a, b, c)
"""

# Кортеж - это то же самое что и списки только не изменяемые


# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.

# В списках в качестве ключа используется индекс элемента. В словаре для
# определения элемента используется значение ключа (строка, число)
"""
dictionary = {} # можно а = {} или d = dict() - создание пустого словаря
dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →
"""
# d = {}
# d['q'] = 'qwerty'
# print(d) # {'q': 'qwerty'}
# d['w'] = 'werty'
# print(d) # {'q': 'qwerty', 'w': 'werty'}
# print(d['q']) # qwerty

# МНОЖЕСТВА
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность
"""
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok
print(colors) # {'green', 'blue','gray'}
colors.clear() # { }
print(colors) # set()
"""

# Операции со множествами в Python
"""
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
"""

# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления
"""
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
"""

# List Comprehension
# У каждого языка программирования есть свои особенности и преимущества. Одна
# из культовых фишек Python — list comprehension (редко переводится на русский, но
# можно использовать определение «генератора списка»). Comprehension легко
# читать, и их используют как начинающие, так и опытные разработчики.
# List comprehension — это упрощенный подход к созданию списка, который
# задействует цикл for, а также инструкции if-else для определения того, что в итоге
# окажется в финальном списке
"""
# 1. Простая ситуация — список:
list_1 = [exp for item in iterable]
# 2. Выборка по заданному условию:
list_1 = [exp for item in iterable (if conditional)]


# 1. Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
"""

# SyntaxError(Синтаксическая ошибка)

number_first = 5
number_second = 7
if number_first > number_second  # !!!!! отсутствует двоеточие
    print(number_first)
# Отсутствие :

# IndentationError(Ошибка отступов)
number_first = 5
number_second = 7
if number_first > number_second:
print(number_first) # !!!!!
# Отсутствие отступов

TypeError(Типовая ошибка)
text = 'Python'
number = 5
print(text + number)
# Нельзя складывать строки и числа
● ZeroDivisionError(Деление на 0)
number_first = 5
number_second = 0
print(number_first // number_second)
# Делить на 0 нельзя
KeyError(Ошибка ключа)
dictionary = {1: 'Monday', 2: 'Tuesday'}
print(dictionary[3])
# Такого ключа не существует
NameError(Ошибка имени переменной)
name = 'Ivan'
print(names)
# Переменной names не существует
ValueError(Ошибка значения)
text = 'Python'
print(int(text))
# Нельзя символы перевести в целые значения
