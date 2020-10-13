"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

my_file = open("text.txt", "r")
count_line = 0
count_sign = 1
for line in my_file:
    count_line += 1
    for sign in line:
        if sign == " ":
            count_sign += 1
    print(count_sign)
    count_sign = 1
print(count_line)
