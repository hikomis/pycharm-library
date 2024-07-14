day = int(input('Введите кол-во дней: '))
a = 0
b = 0
for i in range(1,day+1):
    c = int(input(f'Введите температуру в {i} день: '))
    a += c
    if c > 0:
        b += 1
print(f'Средняя температура за время наблюдения {a/day}')
if b >= 5:
    print('YES')
else:
    print('NO')

