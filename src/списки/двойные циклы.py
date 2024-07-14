vagon = int(input("Введите кол-во вагонов: "))
train = []
suma = 0
for i in range(0,vagon):
    people = int(input("Введите количество пассажиров: "))
    train.append(people)
    suma += people
print(train)
print(suma)
