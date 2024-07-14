f = open('17 (2).txt')
a = [int(i) for i in f.readlines()]
count = 0
mx = -120329329
for i in range(0,len(a)):
    for x in range(i,len(a)):
        if (a[x] + a[i]) % 2 == 1 and (a[x] * a[i]) % 3 == 0:
            count += 1
            mx = max(mx,a[x] + a[i])
print(count,mx)