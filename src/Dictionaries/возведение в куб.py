def kub(x):
    return x, x**3
print(dict(kub(x)  for x in range(1,11)))