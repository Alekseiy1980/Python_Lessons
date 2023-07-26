# # # # def sum_numders(n, y ="Hello World"):
# # # #     print(y)
# # # #     summa = 0
# # # #     for i in range (1, n+1):
# # # #         summa += i
# # # #     return (summa)
# # # #
# # # #
# # # # summa = sum_numders(5, "qwerty")
# # # # print(summa)
# # #
# # # def sum_str(*args):
# # #     res = ''
# # #     for i in args:
# # #         res += i
# # #         return  res
# # #
# # #
# # # print(sum_str('q', 'e', 'l'))
# #
# # '''
# # подключение своих файлов(библиотек)
# # '''
# # # # # # import modul1 as m1
# # # # # #
# # # # # # print(m1.max1(51,9))
# # # # #
# # # # # from modul1 import max1
# # # # #
# # # # # print(1,9)
# # # #
# # # # import modul1 as m1
# # # #
# # # # print(m1.max1(13,6))
# # #
# # # from modul1 import*
# # # print(max1(7,134))
# #
# # '''
# # Рекурсия
# # '''
# #
# # def fib(n):
# #     if n in[1,2]:
# #         return 1
# #     return fib(n - 1) + fib(n - 2)
# #
# # list_1 = []
# # for i in range(1,10):
# #     list_1.append(fib(i))
# # print(list_1)
#
# '''
# Быстрая сортировка Quick_sort
# '''
#
# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:]if i <= pivot]
#     greater = [i for i in array[1:]if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([14,5,9,6,2,7,4,3,0,56,73]))

'''
Сортировка слиянием - Merge_sort
'''

def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j +=1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
list_1 = [1,6,0,34,56,12,34,5,6,7,0,3,6]
merge_sort(list_1)
print(list_1)