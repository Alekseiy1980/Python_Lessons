import random
import pandas as pd



lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# print(lst)
lst_robo = []
lst_human = []

for item in lst:
    if item == 'robot':
        lst_robo.append('1')
        lst_human.append('0')
    else:
        lst_robo.append('0')
        lst_human.append('1')

data = pd.DataFrame({'robot': lst_robo, 'human': lst_human})

print(data.head())
