def arithmetic(a,b,h):
    if h =='+':
        return a+b
    elif h =='-':
        return a-b
    elif h =='*':
        return a*b
    elif h =='/':
        return a/b
    elif h =='**':
        return a**b
    else:
        return "Неизвестная операция"


def kalendar(year):
    if year % 4 == 0 and year % 400 == 0 and year % 100 == 0:
        print(year, "29")
    else:
        print(year, "28")

def treug(a,b):
    return a*b*0.5

def cvadrat(a):
    return a*a

def pramoug(a,b):
    return a*b

def parolilep(a,b,c):
    return (a*b+b*c+a*c)*2