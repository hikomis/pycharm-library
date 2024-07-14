number = input("Введите ряд чисел: ").split()
chislo = int(number[0])
for i in range(1,len(number)):
    chislo = max(int(number[i]),chislo)
print(chislo)





a = (list(map(int,number)))
print(max(a))