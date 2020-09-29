new_list = [7, 6, 4, 4, 2]
count = 0
while True:
    new_digit = int(input('Введите число'))
    for i in new_list:
        if new_digit > i:
            list.insert(new_list, count, new_digit)
            count = 0
            break
        elif count == len(new_list)-1:
            list.insert(new_list, count+1, new_digit)
            count = 0
            break
        count += 1
    print(new_list)