"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def user_data(**kwargs):
    return kwargs


print(user_data(name=input('name'), surname=input('surname'), birthday=input('birthday'), city=input('city'),
                email=input('email'), phone=input('phone')))
