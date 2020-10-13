"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

with open("text.txt") as obj_text:

    while True:
        obj_text = open("text.txt", "a+")
        string = (input('input text'))+"\n"
        if string == "\n":
            break
        else:
            obj_text.write(string)
