t = int(input('Введите числа: '))
summa = 0
count = 0
while t != 0:
    count += 1
    if (t % 2 == 0):
        summa += t
    t = int(input('Введите числа: '))

print(f'{count}\n{summa}')