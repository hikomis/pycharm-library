f = open('17 (1).txt')
a = [int(i) for i in f.readlines()]
mx = -30000
count = 0
for x in range(0,len(a)-1):
    if a[x] % 3 == 0 or a[x+1] % 3 == 0:
        count += 1
        if a[x] + a[x+1] > mx:
            mx = a[x] + a[x+1]
print(count,mx)