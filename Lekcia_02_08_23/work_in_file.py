# # colors = ['red', '12345', 'blue']
# # data = open('file.md', 'a')  # здесь указываем режим , в котором будем работать file - название файла , после точки указываем расширение .txt , .md как примеры
# # data.writelines(colors)  # разделителей не будет
# # data.close()
#
#
# '''
# идет перезапись файла и когда функция видит print она закрывает файл и выходит с функции перезаписи
# '''
# with open('file.md', 'w')as data:
#     data.write('Line 1\n')
#     data.write('Line 2\n')
#
# print(56)

'''
режим чтения

'''

path = 'file.md'
data = open(path, 'r')
for line in data:
    print(line)
data.close()