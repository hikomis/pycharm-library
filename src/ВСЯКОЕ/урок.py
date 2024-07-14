number = int(input("Введите число: "))
stepen = int(input("Введите степень числа: "))
output = []
for i in range(0,stepen + 1):
    output.append(number**i)
print(output)