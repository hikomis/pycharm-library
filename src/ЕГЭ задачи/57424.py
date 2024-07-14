f = open('17_5 .txt')
a = [int(i) for i in f.readlines()]
mx = 0
count = 0
mxNum = 0
for i in range(0,len(a)):
    if 9 < a[i] < 100:
        mxNum = max(mxNum,a[i])
for x in range(0,len(a)-1):
    if (a[x] + a[x+1]) % mxNum == 0:
        count += 1
        mx = max(mx,(a[x] + a[x+1]))
print(count,mx)
