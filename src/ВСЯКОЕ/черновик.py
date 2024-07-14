def mySqr(x):
    if x == 0 or x == 1:
        return x
    res = 0
    while 1 <=r:
        m = (start + end)//2
        s = m * m
        if s == x:
            return  m
        if s <x :
            start = m+1
            ans = m
        else:
            end = m -1
            return ans
print(mySqr(15))