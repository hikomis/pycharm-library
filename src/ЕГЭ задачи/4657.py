def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2 * G(n-1) + 5 * n
def G(n):
    if n == 1:
        return 1
    elif n > 1:
        return F(n-1) + 2 * n
t = F(4) + G(4)
print(t)


