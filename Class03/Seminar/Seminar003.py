

# Дан список чисел. Определите, сколько в нем встречается различных чисел
"""
# list = [1, 5, 1, 2, 3, 4, 5, 2]
numbers = [input () for i in range(int(input()))]
# for i in range (6):
    # numbers.append(input()) - добавление чисел в конец списка
print(len(set(numbers)))
"""
"""
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.
list_nums = [1, 2, 3, 4, 5]
k = int(input('Введите K: '))
for i in range (k):
    list_nums.insert(0, list_nums.pop(-1)) # list_nums.pop()) без -1 все равно удаляет последний элемент
    print(list_nums)
"""
"""
# Напишите программу для печати всех уникальных значений в словаре.
list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {"V": " S009 "}, {"VIII": " S007 "}]

print(set([list(i.values())[0].strip() for i in list_dict]))
# или
n_list = []
for i in list_dict:
    w_list = list(i.values())
    word = w_list[0]
    word_clear = word.strip()
    n_list.append(word_clear)

print(set(n_list))


# list_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
#              {"VI": "S005"}, {"VII": " S005 "}, 
#              {" V ":" S009 "}, {" VIII ":" S007 "}]
# unique_dict_items = set()
# for i in list_dict:
#     for j in i.keys():
#         unique_dict_items.add(i[j])
# print(unique_dict_items)
"""

# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)

list_nums = [0, -1, 5, 2, 3]
res = [list_nums[i] > list_nums[i - 1] for i in range(1, len(list_nums))]
print(sum(res))

# или
# count = 0

# for i in range(1, len(array) - 1) :
#     if(array[i + 1] > array[i]) :
#         count += 1
    
# print(count)