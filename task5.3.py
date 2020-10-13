"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

text = open("person1.txt", "r")
personal_dict = {}
i = 0
summa = 0
while True:
    pers = text.readline().split()
    if not pers:
        break
    summa += int(pers[1])
    if int(pers[1]) < 20000:
        print(pers[0])
    i += 1
print(f'Средняя ЗП равна: {summa / i:.2f}')
text.close()