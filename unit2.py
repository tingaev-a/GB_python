time_in_seconds = int(input('Введите время в секундах'))

hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours * 3600) // 60
seconds = time_in_seconds - hours * 3600 - minutes * 60

# Проверяем количество знаков в переменной и если менее 2, то переводим в строку и добавляем впереди 0,

if hours < 10:                  # Проверяем количество знаков в переменной
    hours = '0' + str(hours)    # если менее 2, то переводим в строку и добавляем перед ней '0'
else:
    hours = str(hours)          # иначе просто конвертируем в str
if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)

print(f'Это равно {hours}:{minutes}:{seconds}')
