vagon = int(input("Введите кол-во вагонов: "))
gruppa = int(input("Введите кол-во групп в вагоне: "))
deppo = []
num = 0
summa = 0
for i in range(0,vagon):
    k = 0
    deppo.append([])
    for y in range(0,gruppa):
        people = int(input('Введите количество людей в вагоне:'))
        deppo[i].append(people)
        k += people
    if k > summa:
        summa = k
        num = i + 1
print(deppo)
print(summa,num)


