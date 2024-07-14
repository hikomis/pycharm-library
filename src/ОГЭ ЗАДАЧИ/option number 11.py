k = int(input('Введите кол-во чисел: '))
count = 0
for i in range(k):
    k = int(input('введите число: '))
    if k % 6 == 0:
        count += 1
print(count)