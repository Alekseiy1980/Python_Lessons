from  random import  choice

x = choice([True,False])
print (x)


# sp = []
# sp.append(65465)
# sp.append("privet")
# sp.append(4.5)
# sp.append([5,7])
# sp.append(True)
# print(sp)
#
# i=0
# while i<10:
#     print(i, end = " ; ")
#     i +=1
#
# for _ in range(4):
#     print("hello")
#
# for i in sp:
#     print(i

# i = int(input())
# factorial =  1
# count = 1
# while count <= i:
#     factorial *= count
#     count +=1
# print(factorial)

# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# 0 1 1 2 3 5 8


# A = int(input("Enter a number: "))
# i = 2
# febonachi = []
# febonachi.append(0)
# febonachi.append(1)
# while febonachi[i-1] < A:
#     febonachi.append(febonachi[i - 1] + febonachi[i - 2])
#     i += 1
# iter = 0
# while len(febonachi) > iter:
#     if febonachi[iter] == A:
#         print(iter)
#     else:
#         print("-1")
#     iter += 1
# print(i)
# print(febonachi)


#По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = 5
# i = 1
# fak = 1
# if n == 0:
#     fak = 1
# while i <= n:
#     fak = fak*i
#     i += 1
# print(fak)


# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# A = int(input("Введите проверяемое число"))
# #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
#
# current = 1 #текущее
# previous = 0 #предыдущее
#
# i = 2 #
# while current < A:
#     temporary = current
#     current = previous + current
#     previous = temporary
#     i = i + 1
# #print(current)
# if current == A:
#     print(i)
# else:
#     print(-1)


# N = int(input( "Введите рассматриваемые дни 1 < N <100"))
# sp = []
# i = 0
# for _ in range (N):
#     sp.append(int(input("Введите температуру от - 50 до ")))
# max_day = 0
# temp_day = 0
# for j in sp:
#     if j > 0:
#         temp_day = temp_day + 1
#
#         if max_day < temp_day:
#             max_day = temp_day
#
#     else:
#         temp_days = 0
# print (max_day)
#
# N = int(input("Введите общее количество рассматриваемых дней 1 ≤ N ≤ 100: "))
# sp = []
# i = 0
# for _ in range(N):
#     sp.append(int(input("Введите тепературу от -50 до 50 ")))
#
# max_days = 0
# temp_days = 0
# for j in sp:
#     if j > 0:
#         temp_days = temp_days + 1
#         if max_days < temp_days:
#             max_days = temp_days
#     else:
#         temp_days = 0
# print(max_days)


# N = int(input("Введите кол-во арбузов  "))
# sp = []
# i = 0
# for _ in range(N):
#     sp.append(int(input("Масса арбуза  ")))
# min = sp[0]
# max = sp[0]
# for j in sp:
#     if(j < max):
#         max = j
#     if(j>min):
#         min = j
# print( min , max)