# x: int = "Привет"
# y: int = 3
# # print(x+y)
#
# def summa(x1, x2):
#     print (x1 + x2)
#
# def summa2(x1: int, x2: int) -> int:
#     global x
#     res: int = x1 +x2
#     x = x + " алоха "
#     return res
#
#
#
#
# a = summa2(4,9)
# print(a)
# print(summa2("hello"," world"))
# print(x)
# summa(8,12)

# '''
# Задача 25
# Напишите программу ,которая принимает на вход строку ,и отслеживает
# сколько раз каждый символ уже встречался. Количество повторов добявляется
# символом с помощью постфикса формата _n
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#
# для решения используйте функцию .split()
# '''
# sp = "a a a b c a a d c d d"
# new_list = sp.split()
# new_ar = {}
# result = ""
# for i in new_list:
#     if i not in new_ar:
#         new_ar[i] = 0
#         result += f"{i} "
#     else:
#         new_ar[i] += 1
#         result += f"{i}_{new_ar[i]} "
#
# print(result)

'''
задача 27
Определить сколько различных слов содержится в тексте
'''

