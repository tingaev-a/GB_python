new_list = (str.split((input('Введите предложение')), ' '))
num = 1
for i in new_list:

    if len(i) > 9:
        i = i[0:10]
    print(f'', num, i)
    num += 1
