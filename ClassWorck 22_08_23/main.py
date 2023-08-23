'''

Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

'''

import json


telephone_books = []



def load():
    with open("telephone_book.json","r",encoding="utf-8") as tb:
        telephone_book = json.load(tb)
    return  telephone_book

def save():
    with open("telephone_book.json", "w", encoding="utf-8") as tb:
        tb.write(json.dumps(telephone_books, ensure_ascii=False))
    print("Телефонная книга успешно сохранена")



while True:
    command = input("Введите команду")
    if command ==  "/add":
        name = input("Введите имя нового контакта: ")
        number0 = input("Введите 1й номер: ")
        number1 = input("Введите 2й номер: ")
        birth_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        telephone_books[name] = {"telephone":[number0,number1],"email":mail, "birth_day": birth_day}
    elif command == "/all":
        print("Список контактов")
        print(telephone_books)
    elif command == "/find":
        name = input("Введите имя для поиска: ")
        if name in telephone_books:
            print(telephone_books[name])
    elif command == "/save":
        save()
    elif command == "/load":

        telephone_books = load()
        print ("Файлы успешно загружены")
    elif command == "/stop":
        save()
        print("пока")
        break

