# def Summ(num):
#     if num == 0:
#         return num
#     return num + Summ(num - 1)
#
# sum = Summ(5)
# print(sum)

# def fib(num):
#     if num == 0 or num == 1:
#         return num
#     return fib(num - 2) + fib(num - 1)
#
# n = int(input())
# print(fib(n))

'''

Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

'''

from random import randint

def init(num):
    sp = [randint(1, 5) for i in range(num)]
    return sp

def renaim(sp, i = 0):
    if i == len(sp):
        return sp
    if sp[i] == max(sp):
        sp[i] = min(sp)
    renaim(sp, i+1)


count = int(input("Колличество оценок "))
sp = init(count)
print(sp)
renaim(sp)
print(sp)

# def rekursia (num, i = 0):
# if i == len(num):
# return num
# if num[i] == max(num):
# num[i] = min(num)
# rekursia(num, i + 1)
#
#
#
#
# x = [1, 3, 4, 3, 4]
# rekursia(x)
# print(x)