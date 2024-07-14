def F(n):
    if n <= 2:
        return n
    elif n > 2:
        return F(n-1) + 2 * F(n-2)
print(F(6))