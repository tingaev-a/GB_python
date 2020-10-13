"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
import random

text = open("num.txt", "w")
for i in range(10):
    num = str(int(random.random()*100))
    text.write(num)
    text.write(" ")
text.close()

text = open("num.txt", "r")
num_str = str.split(text.readline())
print(num_str)
num = 0
for i in num_str:
    i = int(i)
    num += i
print(num)
text.close()