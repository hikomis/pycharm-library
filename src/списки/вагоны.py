vagon = int(input("Введите кол-во вагонов: "))
train = []
suma = 0
for i in range(0,vagon):
    gruppa = int(input('Введите количество групп в вагоне:' ))
    train.append([])
    for y in range(0,gruppa):
        people = int(input("Введите количество людей в группе: "))
        train[i].append(people)
print(train)