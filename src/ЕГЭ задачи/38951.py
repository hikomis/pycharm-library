f = open('17_122.txt')
a = [int(i) for i in f.readlines()]
count = 0
mx = 0
for i in range(0,len(a)-1):
    if (a[i] % 3 == 0 or a[i+1] % 3 == 0) and (a[i] + a[i+1]) % 5 == 0:
            count += 1
            mx = max(mx,a[i] + a[i+1])
print(count,mx)