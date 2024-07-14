print("калькулятоор")
perem_1 = int(input("Введите первое число\n"))
sign = int(input("Введите знак: 1)+, 2)-, 3)*, 4)/\n"))
perem_2 = int(input("Введите второе число\n"))
if sign == 1:
    itog = perem_1 + perem_2
    print(perem_1, "+", perem_2, "=", itog)
elif sign == 2:
    itog = perem_1 - perem_2
    print(perem_1, "-", perem_2, "=", itog)
elif sign == 3:
    itog = perem_1 * perem_2
    print(perem_1, "*", perem_2, "=", itog)
elif sign == 4:
    itog = perem_1 / perem_2
    print(perem_1, "/", perem_2, "=", itog)


