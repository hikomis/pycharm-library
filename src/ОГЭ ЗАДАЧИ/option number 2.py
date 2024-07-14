k = 1
summa = 0
while k != 0:
    k = int(input('Введите число: '))
    if k == 0:
        break
    if k % 3 == 0 and k % 10 == 9:
        summa += k
print(summa)
