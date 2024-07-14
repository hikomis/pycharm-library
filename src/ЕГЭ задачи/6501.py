def F(n):
    if n <= 2:
        return n + 1
    elif n > 2:
        return F(n-1) * F(n-2)
print(F(4))