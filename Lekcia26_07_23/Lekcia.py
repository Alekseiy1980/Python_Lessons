# # def sum_numders(n, y ="Hello World"):
# #     print(y)
# #     summa = 0
# #     for i in range (1, n+1):
# #         summa += i
# #     return (summa)
# #
# #
# # summa = sum_numders(5, "qwerty")
# # print(summa)
#
# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#         return  res
#
#
# print(sum_str('q', 'e', 'l'))

'''
подключение своих файлов(библиотек)
'''
# # # # import modul1 as m1
# # # #
# # # # print(m1.max1(51,9))
# # #
# # # from modul1 import max1
# # #
# # # print(1,9)
# #
# # import modul1 as m1
# #
# # print(m1.max1(13,6))
#
# from modul1 import*
# print(max1(7,134))

'''
Рекурсия
'''

def fib(n):
    if n in[1,2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)