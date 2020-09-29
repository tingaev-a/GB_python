num_month = int(input('Введите номер месяца'))
full_seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(full_seasons[num_month-1])
num_seasons = (num_month % 12) // 3
min_seasons = ['зима', 'весна', 'лето', 'осень']
print(min_seasons[num_seasons])
dict_seasons = {'0': 'зима', '1': 'весна', '2': 'лето', '3': 'осень'}
print(dict_seasons.get(str(num_seasons)))
