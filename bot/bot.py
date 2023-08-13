from random import *
import json

films = []

def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
    print("Наша фильмотека была успешно сохранена в файле films.json")

def load():
    with open("films.json", "r", encoding="utf-8") as fh:

        films = json.load(fh)
    print("Фильмотека была успешно загружена ")

try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека была успешно загружена ")
except:
    # films = []
    films.append("Матрица")
    films.append("Девять негретят")
    films.append("Мортал-Комбат")
    films.append("Санта Барбара")


while True:
    command = input("Введите команду  ")
    if command == "/start":
        print("Бот фильмотека начал работать  ")
    elif command == "/stop":
        save()
        print("Рад был помочь Вам!")
        print("Буду рад вам помочь в следующий раз")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(*films)
    elif command == "/help":
        print("/Start - начало работы бота ")
        print("/Stop - закончить работу бота ")
    elif command == "/add":
        f = input("Введите название фильма  ")
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию ")
    elif command == "/del":
        f = input("Введите название фильма который вы хотите удалить ")

        '''
        # if f == films:
        #     films.append(f)
        #     print("Фильм успешно удален из фильмотеки ")
        # else:
        #     print("Такого фильма нет ")
        '''

        try:
            films.append(f)
            print("Фильм успешно удален из фильмотеки ")
        except:
            print("Такого фильма нет ")
    elif command == "/random":
        '''
        rnd = randint(0, len(films) - 1)
        print(films[rnd])
        '''
        print(choice(films))
    elif command == "/save":
        save()
    elif command == '/load':
        load()

    else:
        print("Вы ввели неправильную команду. С командами можно ознакомиться набрав команду /Help")
