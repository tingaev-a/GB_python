keys = ('Название', 'Цена', 'Количество', 'Ед.')    # потом заменить на ввод
value = []
goods = []
d1 = {}
one_item = []
for i in range(1, 4):   # переделать на while и поставить условие выхода
    list.clear(value)   # чистим список ввода для следующего словаря
    one_item = list(one_item)   # преобразуем кортеж обратно в список для очистки и переиспользования
    list.clear(one_item)
    for j in range(0, len(keys)):   # ввод значений в словарь
        print(f'Введите', keys.__getitem__(j))
        list.append(value, input(''))
    print(value)
    d1 = dict.fromkeys(keys)
    count = 0
    for k in keys:
        d1[k] = value[count]
        count += 1
    list.append(one_item, i)
    list.append(one_item, d1)
    print(one_item)
    one_item = tuple(one_item)
    print(one_item)
    list.append(goods, one_item)

    print(goods)

select = {}
for l in goods:
    for m, n in l[1].items():
        if m not in select:
            select[m] = []
        select[m].append(n)

print(select)


