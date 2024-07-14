count = 0
k = 1
while k != 0:
    k = int(input('Введите число: '))
    if k / 10 == 0 and k % 3 == 0:
        count += 1
print(count)