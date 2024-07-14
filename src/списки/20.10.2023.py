while True:
    a = (input("Ведите ряд чисел через пробел: ")).split()
    b = int(input("Выберите желанную операцию:  1-add 2-insert 3-remove 4-Shiftleft 5-Shiftright: "))
    if b == 1:
        number = input("Введите число которое хотите поместить в конец: ")
        a.append(number)
    elif b == 2:
            index = int(input("Введите индекс куда хотите поместить число: "))
            number = (input("Введите число : "))
            a.insert(index,number)
            print(a)
    elif b == 3:
        number2 = (input("Введите число которое хотите удалить: "))
        a.remove(number2)
        print(a)
    elif b == 4:
        num2 = int(input("Введите количество желаемых сдвигов: "))
        for i in range(num2):
            k = a[0]
            for y in range(len(a)):
                if y != 0 and y != len(a) - 1:
                    a[y - 1] = a[y]
                    a[y] = a[y + 1]
                else:
                    a[y] = k
    elif b ==5:
        num7 = int(input("Введите количество желаемых сдвигов: "))
        for i in range(num7):
            k = a[0]
            for y in range(len(a)):
                if y != 0 and y != len(a) - 1:
                    a[y - 1] = a[y]
                    a[y] = a[y + 1]
                else:
                    a[y] = k




