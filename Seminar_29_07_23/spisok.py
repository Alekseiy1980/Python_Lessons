from random import randint
# # #
# # # def square(sp):
# # #     res = []
# # #     for item in sp:
# # #         res.append(item**2)
# # #     return res
# # #
# # # def find4_and_square(sp):
# # #     res = []
# # #     for i in sp:
# # #         if i > 4:
# # #             res.append(i ** 2)
# # #     return  res
# # #
# # # # sp = [1,4,18,2,9]
# # # sp = [randint(1,10) for _ in range(10)]
# # # print(sp)
# # # print(sum(sp))
# # # print(square(sp))
# # # print([item**2 for item in sp])
# # # print(find4_and_square(sp))
# # # print([i ** 2 for i in sp if i > 4])
# #
# #
# # '''
# # задача в группе
# # даны два спичка - размер вводит пользователь
# # вывести в томже порядке первый массив за исключением тех цифр которые имеются во вторм
# #
# # -> 7
# # [1, 3, 1, 5, 7, 12, 0]
# #
# # -> 5
# # [2, 5, 6, 10, 7]
# #
# # <- [1, 3, 1, 12, 0]
# # '''
# #
# # size = int(input("Введите размер первого массива "))
# # sp = [randint(1, 10) for _ in range(size)]
# #
# # size = int(input("Введите размер второго массива "))
# # tmp = [randint(1, 10) for _ in range(size)]
# #
# # print(sp)
# # print(tmp)
# # res = [item for item in sp if item not in tmp]
# # print(res)
#
# '''
#
# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел
# '''
#
# def chek(index,array):
#     if array[(index+1)%len(array)] < array[(index)]and array[(index)]> array[index - 1]:
#         return True
#
#
# size =int(input("Введите размер  "))
# arr = [randint(1,5) for _ in range(size)]
# print(arr)
# # res = [chek(index, arr) for (index, value) in enumerate(arr)]
# res = [1 for index in range(len(arr)) if chek(index, arr)]
#
# print(sum(res))

'''
Задача №43. Общее обсуждение
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 
Вывод:
2
# '''
# def counter(arr):
#     count = 0
#     for i in set(arr):
#         print(i, arr.count(i))
#         count += arr.count(i) // 2
#
#     return count
#
#
# arr =[randint(1, 5) for _ in range(10)]
# print(arr)
# # print(counter(arr))
# print(sum([arr.count(i)//2 for i in set(arr)]))

# Задача №45. Решение в группах# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа# получает на вход одно натуральное число k, не
# превосходящее 105# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть# выведена только один раз (перестановка чисел новую
# пару не дает).# Ввод:
# 300# Вывод:
# 220 284
k = int(input("Введите число k: "))

def deliteli(value):
    deliteli = []
    for num in range(1, value // 2 + 1):
        if value % num == 0:
            deliteli.append(num)
    return deliteli


for m in range(2, k):
    n = sum(deliteli(m))
    if m == sum(deliteli(n)) and m < n:
         print(m, n)