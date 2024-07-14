def r(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n > 3:
        return r(n-3) + r(n-2)
print(r(12))