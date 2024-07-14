shops ={}
while True:
    shop = input("Введите  магазин: ").split()
    if shop[0] == 'Revision':
        break
    else:
        if shop[0] in shops.keys():
            shops[shop[0]].append(shop[1])
        else:
            shops.update({shop[0]:[]})
            shops[shop[0]].append(shop[1])



for i in shops.keys():
    print(i,'->')
    d = shops.get(i)
    for y in d:
        print(f'product:{y}')
#добавить цену


