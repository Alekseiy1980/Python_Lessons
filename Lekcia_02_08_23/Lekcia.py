# # # # n = [1,2,3,4,5,6,7,8,9]
# # # # a = list()
# # # # for i in n:
# # # #     if i % 2 == 0:
# # # #         a.append([i,i**2])
# # # # print(a)
# # #
# # # def select(f,col):
# # #     return [f(x) for x in col]
# # #
# # # def where(f, col):
# # #     return [x for x in col if f(x)]
# # #
# # # data = [1, 2, 3, 5, 8, 15, 23, 38]
# # # res = select(int, data)
# # # print(res)
# # # res = where(lambda x: x%2 == 0,res)
# # # print(res)
# # # res = list(select(lambda x:(x,x**2),res))
# # # print(res)
# #
# '''
# второй вариант
#
# '''
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x%2 == 0,res)
# print(res)
# res = list(map(lambda x:(x,x**2),res))
# print(res)

# '''
#  третий вариант
#
# '''
#
#
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x%2 == 0,res)
# res = list(map(lambda x:(x,x**2),res))
# print(res)



# # list_1= [x for x in range(1, 20)]
# # print(list_1)
# #
# # list_1 = list(map(lambda x: x+10, list_1))
# # print(list_1)
#
# '''
# задача
# '''
# data = '15 23 51 1 5 3 8 65 76'
# print(data)
# '''
# первый вариант со строки переделать в список
#
#
# data = data.split()
# print(data)
# '''
#
# '''
# второй вариант через map
# '''
#
# data = list(map(int, data.split()))

# ///////////////////////////////////////////////
# '''
#
# Фильтр
#
# '''
# data = [15, 56, 65, 9, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)