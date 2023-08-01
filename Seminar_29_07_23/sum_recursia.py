# # # def Summ(num):
# # #     if num == 0:
# # #         return num
# # #     return num + Summ(num - 1)
# # #
# # # sum = Summ(5)
# # # print(sum)
# #
# # # def fib(num):
# # #     if num == 0 or num == 1:
# # #         return num
# # #     return fib(num - 2) + fib(num - 1)
# # #
# # # n = int(input())
# # # print(fib(n))
# #
# # '''
# #
# # Задача №33. Решение в группах
# # Хакер Василий получил доступ к классному журналу и
# # хочет заменить все свои минимальные оценки на
# # максимальные. Напишите программу, которая
# # заменяет оценки Василия, но наоборот: все
# # максимальные – на минимальные.
# # Input: 5 -> 1 3 3 3 4
# # Output: 1 3 3 3 1
# #
# # '''
# #
# # from random import randint
# #
# # def init(num):
# #     sp = [randint(1, 5) for i in range(num)]
# #     return sp
# #
# # def renaim(sp, i = 0):
# #     if i == len(sp):
# #         return sp
# #     if sp[i] == max(sp):
# #         sp[i] = min(sp)
# #     renaim(sp, i+1)
# #
# #
# # count = int(input("Колличество оценок "))
# # sp = init(count)
# # print(sp)
# # renaim(sp)
# # print(sp)
# #
# # # def rekursia (num, i = 0):
# # # if i == len(num):
# # # return num
# # # if num[i] == max(num):
# # # num[i] = min(num)
# # # rekursia(num, i + 1)
# # #
# # #
# # #
# # #
# # # x = [1, 3, 4, 3, 4]
# # # rekursia(x)
# # # print(x)
# # '''
# # юольшая корпорация. посчитать сотрудников
# # '''
# def count(element):
#     if type(element) == int:
#         return element
#     summa = 0
#     for elem in element:
#         if type(element) == list:
#             summa += count(elem)
#         else:
#             summa += elem
#     return summa
#
#
#
# count_angola = 18
# count_new_york = [25, [10, 7]]
# count_chicago = 15
# count_usa = [count_new_york,count_chicago ]
# count_all = [count_angola, count_usa]
# print(count_all)
#
# print(count(count_all))
# '''
# второй авриант решения подсчета сотрудников
# '''
#
#
#
# def count(element):
#     if type(element) == int:
#         return element
#
#     summa = 0
#     for elem in element:
#         summa += count(elem)
#     return summa
#
#
#
# count_angola = 18
# count_new_york = [20, [10, 7]]
# count_chicago = 15
# count_usa = [count_new_york, count_chicago ]
# count_all = [count_angola, count_usa]
# print(count_all)
# print(count(count_all))
# '''
# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
# '''
# # def simple_number(number, input_num):
# #     if number <= 1:
# #         return True
# #     elif input_num % number == 0:
# #         return False
# #
# #     return simple_number(number - 1, input_num)
# #
# #
# #
# # num = int(input("Input number "))
# # print(simple_number(num - 1, num))
#
#
#
#
#
# '''
# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# '''
#
# def revers(count):
#     i = 0
#     if count == 0:
#         return i
#     else:
#         i = int(input("Input num  "))
#
#     return revers(count - 1)
#
# n = int(input("num  "))
# print(revers(n))