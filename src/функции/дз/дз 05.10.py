num = (input("Введите список: ")).split()
num2 = int(input("Введите количество желаемых сдвигов: "))
for i in range(num2):
    k = num[0]
    for y in range(len(num)):
        if y != 0 and y != len(num)-1:
            num[y-1] = num[y]
            num[y] = num[y+1]
        else:
            num[y] = k


print(num)