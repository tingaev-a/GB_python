start_distantion = float(input('Введите стартовый результат'))
target_distantion = float(input('Введите целевой результат'))
while target_distantion < start_distantion:
    target_distantion = float(input('Ставьте более амбициозные цели!'))

actual_distantion = start_distantion
count_day = 1
while actual_distantion < target_distantion:
    actual_distantion = actual_distantion * 1.1
    count_day += 1
print(f'Цель будет достигнута на {count_day}-й день')