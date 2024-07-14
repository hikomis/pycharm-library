count = 0
s = input('Введите число: ').split()
for i in range(0,len(s)):
    if i > 100 or int(s[i]) > 30000:
        print('Не соответствует условию задачи')
        break
    if int(s[i]) % 10 == 9:
        count += 1
print(count)