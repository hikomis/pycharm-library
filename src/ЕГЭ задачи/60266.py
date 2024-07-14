f = open('60266.txt').readline()
a = []
for i in range(len(f)):
    if f[i] == 'T':
        a.append(i)
mx = max(a[i+101] - a[i] - 1 for i in range(len(a)-101))
print(mx)

