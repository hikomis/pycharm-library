summa = 0
number = input('Введите числа: ').split()
for i in range(0,len(number)):
    if int(number[i]) % 6 == 0:
        summa += int(number[i])
print(summa)