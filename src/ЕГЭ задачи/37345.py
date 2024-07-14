f = open('17_4.txt')
a = [int(i) for i in f.readlines()]
count = 0
mx = 0
for i in range(0,len(a)):
    for x in range(i,len(a)):
        if (a[x] * a[i]) % 62 == 0:
            count += 1
            mx = max(mx,(a[x] + a[i]))

print(count,mx)

