product = [[],[]]
while True:
    tovar = (input("Введите название товара: "))
    if tovar == 'end':
        break
    elif tovar in product[0]:
        print("данный товар уже имеется")
    else:
        number = int(input("Введите количество товара: "))
        product[0].append(tovar)
        product[1].append(number)

while True:
    tovar = (input("Введите название нужного товара: "))
    if tovar == "stop":
        break
    elif tovar in product[0]:
        number = int(input("Введите количество товара: "))
        k = product[0].index(tovar)
        if product[1][k] >= number:
            product[1][k] -= number
            print("вы купили",tovar,"в количестве",number)
        else:
            print("Больше чем есть в наличии")
    else:
        print("Данный товар отсутствует")

for i in range(0,len(product[0])):
    print(product[0][i], "осталось", product[1][i])









