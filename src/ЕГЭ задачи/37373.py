f = open('17_66.txt')
a = [int(i) for i in f.readlines()]
mx = 0
count = 0
for i in range(0,len(a)-1):
    for x in range(i+1,len(a)):
        if (a[i] - a[x]) % 36 == 0 and (a[i] % 36 == 0 or a[x] % 36 == 0):
            count += 1
            mx = max(mx,(a[i] - a[x]))
print(count,mx)
