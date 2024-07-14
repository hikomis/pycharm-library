f = open('1_17.txt')
a = [int(i) for i in f.readlines()]
mx = - 40000
count = 0
for i in range(0,len(a)-2):
    if a[i+1] % 100 == 17:
        mx = max(mx,a[i+1])
for x in range(0,len(a)-2):
    if a[x] > 99 and a[x] < 1000:
        if a[x+1] < 99 or a[x+1] > 1000 and (a[x+2] < 99 or a[x+2] > 1000) and (a[x] + a[x+1] + a[x+2] < mx):
           count += 1
    elif (a[x+1] > 99 and a[x+1] < 1000) and (a[x+2] < 99 or a[x+2] > 1000) and (a[x] + a[x+1] + a[x+2] < mx):
        count += 1
    elif (a[x+2] > 99 and a[x+2] < 1000) and (a[x+1] < 99 or a[x+1] > 1000) and (a[x] + a[x+1] + a[x+2] < mx):
        count += 1
    elif a[x+1] < -99 or a[x+1] > -1000 and (a[x+2] < -99 or a[x+2] > -1000) and (a[x] + a[x+1] + a[x+2] < mx):
           count += 1
    elif (a[x+1] > -99 and a[x+1] < -1000) and (a[x+2] < -99 or a[x+2] > -1000) and (a[x] + a[x+1] + a[x+2] < mx):
        count += 1
    elif (a[x+2] > -99 and a[x+2] < -1000) and (a[x+1] < -99 or a[x+1] > -1000) and (a[x] + a[x+1] + a[x+2] < mx):
        count += 1

print(count)