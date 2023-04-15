

# Дан список чисел. Определите, сколько в нем встречается различных чисел

list = [1, 5, 1, 2, 3, 4, 5, 2]
# # b = 0
# # for i in list:
# #     b += 1
# # print(b)
# print(list.count(1))
list = len(set(list))
