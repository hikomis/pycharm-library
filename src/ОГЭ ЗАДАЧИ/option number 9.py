count = 0
summa = 0
t = 1
while t != 0:
    t = int(input('Введите числа: '))
    if t == 0:
        break
    if t % 8 == 0:
        summa += t
        count += 1
if count > 0:
    print(round(summa/count, 1))
else:
    print('NO')



