a = []
number = input("Введите ряд чисел: ").split()
for i in number:
    summa = 0
    pro = 1
    for y in range(len(i)):
        summa += int(i[y])
        pro *= int(i[y])
    if summa == pro:
        a.append(i)
print(*a)



