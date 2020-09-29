old_list = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e', 6, 'f', 7, 'g', 8, 'h', 9, 'i', 10]
half_len = len(old_list) // 2

for i in range(0, half_len*2, 2):
    j = i+1
    temporal_item = old_list[j]
    old_list[j] = old_list[i]
    old_list[i] = temporal_item
print(old_list)
