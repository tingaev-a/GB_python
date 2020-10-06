"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
num1 = float(input('Введите числитель'))
num2 = float(input('Введите знаменатель'))

def division (arg1, arg2):
    try:
        div = (arg1 / arg2)
    except ZeroDivisionError:
        return ('Деление на 0')
    return div


print(division(num1, num2))
