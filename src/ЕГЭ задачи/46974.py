def F(n):
    if n == 0:
        return 0
    elif n % 2 != 0:
        return F(n-1) + 1
    elif n % 2 == 0 and n > 0:
        return F(n/2)
count = 0
n = 0

while n < 1000000000:
    if F(n) == 2:
        count += 1
        print(count)
    n += 1

print(count)