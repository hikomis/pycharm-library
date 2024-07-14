def F(n):
    if n >= 2025:
        return n
    elif n < 2025:
        return n + F(n+2)
t = F(2022) - F(2023)
print(t)
