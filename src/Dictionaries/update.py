product = {}
while True:
    tovar = (input("Введите название товара: "))
    if tovar == 'end':
        break
    elif tovar in product.keys():
        print("данный товар уже имеется")
    else:
        number = int(input("Введите количество товара: "))
        product.update({tovar:number})

while True:
    tovar = (input("Введите название нужного товара: "))
    if tovar == "stop":
        break
    elif tovar in product.keys():
        number = int(input("Введите количество товара: "))
        k = product.get(tovar)
        if k >= number:
            product.update({tovar:k - number})
            print("вы купили",tovar,"в количестве",number)
        else:
            print("Больше чем есть в наличии")
    else:
        print("Данный товар отсутствует")

for i in product.keys():
    print(i,"осталось",product.get(i))




