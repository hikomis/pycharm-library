k = 1
count = 0
while k != 0:
    k = int(input('Введите число: '))
    if k == 0:
        break
    if k % 2 == 0 and k % 5 == 0:
        count += 1
print(count)