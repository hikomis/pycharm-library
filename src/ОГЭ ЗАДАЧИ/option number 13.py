summa = 0
k = 1
while k > 0:
    k = int(input('Введите число: '))
    if k == 0:
        break
    elif k % 6 == 0 and k % 10 == 2:
        summa += k
print(summa)