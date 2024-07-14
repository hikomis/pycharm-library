number = (input("Введите ряд чисел: " )).split()
for i in range(0,len(number),2):
    if int(number[i]) > 100:
        print(number[i])