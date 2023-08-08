# # # # # # # # def creat_phase(func, word):
# # # # # # # #     print(func(word))
# # # # # # # #
# # # # # # # # def hello(s):
# # # # # # # #     return f"hello {s}"
# # # # # # # #
# # # # # # # # def bay(s):
# # # # # # # #     return f"{s} bay-bay"
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # creat_phase(hello, "world")
# # # # # # # # creat_phase(hello, 'Алексей')
# # # # # # # # creat_phase(bay,'word')
# # # # # # # # creat_phase(bay, 'Aleks')
# # # # # # #
# # # # # # #
# # # # # # # def calc_power(dgree):
# # # # # # #     def pawer(number):
# # # # # # #         return number ** dgree
# # # # # # #     return pawer
# # # # # # #
# # # # # # #
# # # # # # # print(calc_power(2)(3))
# # # # # # # square = calc_power(2)
# # # # # # # # print(id(square))
# # # # # # # cube = calc_power(3)
# # # # # # # # print(id(calc_power(2)))
# # # # # # # print(square(8))
# # # # # # # print(cube(3))
# # # # # #
# # # # # # # print((lambda x, y: x + y)(5, 8))
# # # # # # calc = {'+': lambda x, y: x + y,
# # # # # #         '-': lambda x, y: x - y,
# # # # # #         '*': lambda x, y: x * y,
# # # # # #         '/': lambda x, y: x / y
# # # # # #         }
# # # # # #
# # # # # # print(calc['+'](5, 15))
# # # # # # print(calc['*'](5, 300))
# # # # #
# # # # #
# # # # sp = [3, 5, 5, 7, 2]
# # # # # print(*map(lambda item: item ** 2, sp))
# # # # # print(list(map(lambda item: item ** 2 if item > 4 else 0, sp)))
# # # #
# # # # print(*filter(lambda item: True if item > 4 else False,sp))
# # # # print(list(filter(lambda item: True if item > 4 else False,sp)))
# # # # print(*filter(lambda item: item > 4, sp))
# # # # print(list(filter(lambda item: item > 4, sp)))
# # # # print(*sp)
# # # # print(sp)
# # #
# # #
# # # # sp = [3, 5, 15, 7, 2]
# # # # for i, v in enumerate(sp):
# # # #         print(i, v)
# # #
# # #
# # # name = ['Петя', 'Вася']
# # # sp = [3, 5, 15, 7, 2]
# # #
# # # for x1,x2 in zip(name, sp):
# # #         print(x1, x2)
# # #
# # '''
# #
# # Задача №47. Решение в группах
# # У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# # программы используется множество раз и вы не хотите ничего сломать):
# # transformation = <???>
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # transormed_values = list(map(transformation, values))
# # Единственный способ вашего взаимодействия с этим кодом - посредством задания
# # функции transformation.
# # Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# # список значений, а нужно получить его как есть.
# # Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# # копией values.
# # Пример ввода и вывода данных представлены на следующем
# # слайде
# #
# # Задача №47. Решение в группах
# # Ввод:
# # values = [1, 23, 42, ‘asdfg’]
# # transformed_values = list(map(trasformation, values))
# # if values == transformed_values:
# #  print(‘ok’)
# # else:
# #  print(‘fail’)
# # Вывод:
# # ok
# # '''
# #
# # # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# # # print(values)
# # # transform_values = list(map(lambda item: item, values))
# # # print(transform_values)
# # # print([item for item in values])
# # '''
# # Задача №49. Решение в группах
# # Планеты вращаются вокруг звезд по эллиптическим орбитам.
# # Назовем самой далекой планетой ту, орбита которой имеет
# # самую большую площадь. Напишите функцию
# # find_farthest_orbit(list_of_orbits), которая среди списка орбит
# # планет найдет ту, по которой вращается самая далекая
# # планета. Круговые орбиты не учитывайте: вы знаете, что у
# # вашей звезды таких планет нет, зато искусственные спутники
# # были были запущены на круговые орбиты. Результатом
# # функции должен быть кортеж, содержащий длины полуосей
# # эллипса орбиты самой далекой планеты. Каждая орбита
# # представляет из себя кортеж из пары чисел - полуосей ее
# # эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# # где a и b - длины полуосей эллипса. При решении задачи
# # используйте списочные выражения. Подсказка: проще всего
# # будет найти эллипс в два шага: сначала вычислить самую
# # большую площадь эллипса, а затем найти и сам эллипс,
# # имеющий такую площадь. Гарантируется, что самая далекая
# # планета ровно одна
# # Пример ввода и вывода данных представлены на
# # следующем слайде
# #
# # Задача №49. Решение в группах
# # Ввод:
# # orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10
# # '''
# # from math import pi
# # # S = pi*a*b,
# # # где a и b - длины полуосей эллипса
# # def find_farthest_orbit(orbits):
# #        s = list(map(lambda item: pi*item[0]*item[1] if item[0] != item[1] else 0, orbits))
# #        return f"самая далекая планета имеет индекс {s.index(max(s))}"
# # orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(find_farthest_orbit(orbits))
#
#
# '''
# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)
# '''
#
# # print(list(filter(lambda item: True if item > 4 else False,sp)))
# def same_by(characteristic, objects):
#     new = list(filter(characteristic, objects))
#     print(new)
#
#     if new == objects:
#         return True
#
#     return False
# def char(x):
#     return x%2==0
#
#
#
#
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
#
#
# print(same_by(char,values))
# '''
# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов, указание валют счетов,
# соответствующее состояние счетов. То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.
#
# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99
#
# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент, далее надо применить ее в комбинациях с map и zip.
#
#   На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.
# '''

# # # # # # # def calc_power(dgree):
# # # # # # #     def pawer(number):
# # # # # # #         return number ** dgree
# # # # # # #     return pawer
def balans_calc(balances):
    def power(kyrs):
        return balances * kyrs
    return power

def calc(sp):
    dollar = 90
    euro = 99
    for item in sp:
        if item[1] =='доллар':
            balans_calc(dollar)
        else:
            balans_calc(euro)
    return sp

def list_zip(name, currence_name, balances):
    sp = []
    for n,c,b in zip(name, currence_name,balances):
        sp.append([n,c,b])
    return sp

surnames = ["Иванов", "Карпов", "Иголкин"]
currency_name = ["рубль", "доллар", "евро"]
balances = [30000, 40000, 50000]

sp_zip = list_zip(surnames,currency_name,balances)
print(sp_zip)
