a = []
number = input("Введите ряд чисел: ").split()
for i in number:
    summa = 0
    for y in range(len(i)):
        summa += int(i[y])
    a.append(summa)
print(max(*a))





