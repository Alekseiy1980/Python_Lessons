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


telephone_book = {"Василенко Алексей": {"telephone":[+79014823317, 342543254],"email":"Alekseiy80@mail.ru", "birth_day": "061080"},
                  "Тетя Валя":{"telephone":[5642365432]}}



def save():
    with open("telephone_book.json", "w", encoding="utf-8") as tb:
        tb.write(json.dumps(telephone_book, ensure_ascii=False))
    print("Телефонная книга успешно сохранена")

def load():
    with open("telephone_book.json","r",encoding="utf-8") as tb:
        telephone_book=json.load(tb)
    print("Телефонная книга успешно загружена")



while True:
    command = input("Введите команду")
    if command ==  "/contact":
        name = input("Введите имя нового контакта: ")
        number0 = input("Введите 1й номер: ")
        number1 = input("Введите 2й номер: ")
        birth_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        telephone_book[name] = {"telephone":[number0,number1],"email":mail, "birth_day": birth_day}