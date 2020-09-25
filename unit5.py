proceeds = int(input('Введите размер выручки'))
costs = int(input('Введите размер издержек'))

if costs < proceeds:
    print('Зафиксирована прибыль')
    profit = proceeds - costs
    rentability = profit / proceeds     # Странно, что в ТЗ не было указано что делать с переменной
    personal = int(input('Введите численность персонала'))
    profit_per_person = profit / personal
    print(f'Прибыль на оного сотрудника составила {profit_per_person}')

elif costs > proceeds:
    print('Зафиксирован убыток')

else:
    print('Зафиксирован нулевой баланс')
