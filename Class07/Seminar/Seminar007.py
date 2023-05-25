# enumerate - разбивает список на индекс и значение
"""
list_1 = ['a', 'b', 'c', 'd']

for i, val in enumerate(list_1):
    print(i, val)
"""


"""
nums_list = [int(i) for i in input().split()]
num_min = int(input())
num_max = int(input())

print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])


values = [1, 23, 42, 'asdfg']
transformation = lambda x: x
transformed_values = list(map(transformation, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')
"""

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3), (11, 11)]
print(*find_farthest_orbit(orbits))

12:19
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

def find_farthest_orbit(orbits):
    result = 0
    res = ''
    for i in range(len(orbits)):
        if orbits[i][0] == orbits[i][1]:
            result = result
        else:
            tmp = orbits[i][0] * orbits[i][1]
            if tmp > result:
                result = tmp
                res = orbits[i]
    return res

import  math
def find_farthest_orbit(orbits):
    s_orbits = {math.pi * value[0] * value[1]: value for value in orbits if value[0] != value[1]}
    return max(s_orbits.items())[1]
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))


# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для
# разных объектов отличается - то False.
# Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1
values = [0, 2, 10, 6, 8]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

def same_by(f, a):
    for i in a:
        if f(i):
            return False
    else: 
        return True

# values = [0, 2, 10, 6]
values = [2, 3, 6, 4]


def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# for char in аёеиуояюэы: - так можно пробежаться по гласным