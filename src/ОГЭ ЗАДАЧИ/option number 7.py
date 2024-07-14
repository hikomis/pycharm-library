summa = 0
k = 1
while k != 0:
    k = int(input('Введите числа: '))
    if k % 6 == 0 and k % 10 == 4:
        summa += k
print(summa)