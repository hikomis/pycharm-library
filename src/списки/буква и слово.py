slovo = input("Введите ряд слов: ").split()
bukva = input("Введите букву: ")
number = int(input("Введите количество буквы: "))
spisok = []
for i in slovo:
    k = 0
    for y in range(0,len(i)):
        if i[y] == bukva:
            k += 1
    if k == number:
        spisok.append(i)
print(*spisok)