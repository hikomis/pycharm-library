a = (input("Введите список чисел: ")).split()
b = (input("Введите список чисел: ")).split()
t = []
'''
if a.count(i) > 1:
    d = a.count(i)-1
    for r in range(d, 0, -1):
        a.remove(i)
        print(a)
        print(b)
'''
for i in a:
    for y in b:
        if i == y:
            t.append(i)
            break
print(len(t))
print(t)