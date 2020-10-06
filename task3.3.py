"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(arg1, arg2, arg3):
    numbers = [arg1, arg2, arg3]
    numbers.pop(numbers.index(min(numbers)))
    summary = sum(numbers)
    return summary

print(my_func(float(input('num1')), float(input('num2')), float(input('num3'))))
