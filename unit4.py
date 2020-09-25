num1 = int(input('Введите целое положительное число'))
dig1 = 0

while num1 > 0:
    if dig1 < num1 % 10:
        dig1 = num1 % 10
    num1 = num1 // 10

print(dig1)
