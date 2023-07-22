# from decimal import *


# sp = []
# sp.append(5)
# sp.extend([7,8,True])
# sp.insert(0,5.7)
# sp = sp + [1,2,True,44]
# print(sp)
# # print(sp[3::])
# # print(sp[2:5])
# # print(sp[-5])
# a = sp.pop()
# print(a)
# sp.remove(True)
# del sp[0]

# for i,k in enumerate(sp):
#     print(i,k)
# print(sp)
# t = (4,8,9)
# print(t[0])

# d = {}
# d["дядя Ваня"] = "+78465564"
# d["дядя Вова"] = "12312131"
# del d["дядя Вова"]
# print(d)
# for key, value in d.items():
#     print(key, value)

# print(d.keys())
# print(d.values())

# s = set()
# s.add(5)
# s.add(7)
# print(s)
# print(6 in s)

# list tuple dict set


'''
Задача 17
поиск уникального значения
'''

# list_1 = [1,2,2,4,5,5,6,6,8]
# i = 0
# list_2 = []
# for i in list_1:
#     if i not in list_2:
#         list_2.append(list_1[i])
#
# print(len(list_2))


# data = [1, 1, 2, 0, -1, 3, 4, 4]
# print(data)
# different_numbers = []
# for number in data:
#     if number not in different_numbers:
#         different_numbers.append(number)
# print(f"Различных чисел: {len(different_numbers)}")
#
# l_1 = [1, 2, 3, 4, 5]
# k = 2
#
# print (l_1)
# for i in range (k):
#     a = l_1.pop(len(l_1) - 1)
#     l_1.insert(0, a)
#
# print (l_1)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# v = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
#
# v2 = []
# for i in v:
#     for k,v in i.items():
#         if v.strip() not in v2:
#             v2.append(v.strip())
#             print(k.strip(), v.strip())
#
# print(v2)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)


# v = [0, -1, 5, 2, 3]
# i = 1
# j = 0
# while i < len(v):
#     if v[i] > v[i-1]:
#
#         j+=1
#     i+=1
# print(j)

'''
дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
например был список [1,15,55,7.58,0,99]
и пользователь ввел 5
ответ будет 4
'''
# n = [1,15,55,7.58,0,99]
# i = 0
# count = 0
# while i < len(n):
#     if n[i]//10 or n[i] % 10 == 5:
#         count += 1
#     i += 1
# print(count)

# доп задача для тех кто решил все задачи второй части семинара
# дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4

#
#
# def numbers_after_dot_converter(number):
#     numbers_after_dot = (Decimal(str(number)).as_tuple().exponent * (-1))
#     while numbers_after_dot > 0:
#         number *= 10
#         numbers_after_dot -= 1
#     return round(number)
#
#
# def calc(list):
#     count = 0
#     for i in range(len(list)):
#         while list[i] != 0:
#             if list[i] % 10 == 5:
#                 count += 1
#             list[i] = list[i] // 10
#     return count
#
#
# sp = [1, 15, 55, 7.58, 0, 99]
#
# sp2 = []
# for i in range(len(sp)):
#     sp2.append(numbers_after_dot_converter(sp[i]))
#
# print(sp)
# print(sp2)
# a = calc(sp2)
# print(a)