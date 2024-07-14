spisok = input("Введите ряд чисел: ").split()
while True:
    operation = input("Введите операцию которая вам нужна: ").split()
    if operation[0] == 'Add':
        spisok.append((operation[1]))
        print(spisok)
    elif operation[0] == 'Index':
        f = operation[1]
        d = operation[2]
        spisok.insert(d, f)
        print(spisok)
    elif operation[0] == 'Remove':
        i = operation[1]
        del spisok[i]
        print(spisok)
    elif operation[0] == 'ShiftLeft':
        num2 = operation[1]
        for i in range(num2):
            k = spisok[0]
            for y in range(len(spisok)):
                if y != 0 and y != len(spisok) - 1:
                    spisok[y - 1] = spisok[y]
                    spisok[y] = spisok[y + 1]
                else:
                    spisok[y] = k
        print(spisok)
    elif operation[0] == 'ShiftRight':
        num2 = operation[1]
        for i in range(num2):
            k = spisok[0]
            for y in range(len(spisok)):
                if y != 0 and y != len(spisok) - 1:
                    spisok[y - 1] = spisok[y]
                    spisok[y] = spisok[y + 1]
                else:
                    spisok[y] = k

        print(spisok)


