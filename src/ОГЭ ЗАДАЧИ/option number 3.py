t = input('Введите число: ').split()
summa = 0
for i in range(0,len(t)):
    if int(t[i]) < 300:
        if int(t[i]) % 4 == 0 and int(t[i]) % 10 == 8:
            summa += int(t[i])
print(summa)
