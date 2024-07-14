f = open('17_13.txt')
a = [int(i) for i in f.readlines()]
count = 0
mx = 0
for i in range(len(a)-1):
    for y in range(i+1,len(a)):
        if a[i] * a[y] % 10 == 0:
            count += 1
            mx = max(mx,a[i] + a[y])
print(count,mx)

