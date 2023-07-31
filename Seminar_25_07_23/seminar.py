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
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13
'''
# text= "She sells sea shells on the sea shore The  shells that she sells u h e d  sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# count: int = 0
# text = text.replace('.', ' ').lower().split()
# # new_list = text.split()
# new_arr = {}
#
# for i in text:
#     if i not in new_arr:
#         new_arr[i] = 0
#         count += 1
#     else:
#         new_arr[i] += 1
#
# print(count)
'''
второй вариант решения этой задачи

'''
# text = "She sells sea shells on the sea shore The  shells that she sells   sea shells I'm sure.So if she sells sea shells on the sea sh"
# text = text.replace('.', ' ').lower().split()
# print(len(set(text)))

'''
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам
'''
def max (max_num: int ,i: int) -> int :
    if max_num < i:
        max_num = i
        return  max_num
    return max_num

number: int = -1
max_num: int = 0

while number != 0:
    number = int(input("введите число, 0 - для завершения "))
    max_num = max(max_num, number)
print (max_num)