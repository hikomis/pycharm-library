from rap import arithmetic
print(arithmetic(3,4,'*'))

from rap import kalendar
print(kalendar(2017))

from rap import treug
print(treug(3,5))

from rap import  cvadrat
print(cvadrat(3))

from  rap import parolilep
print(parolilep(3,4,5))

from rap import pramoug


a = int(input('1-трегольник\n2-квадрат\n3-параллелепипед\n4-прямоугольник'))
if a == 1:
    print(treug(int(input()),int(input())))
elif a == 2:
    print(cvadrat(int(input())))
elif a == 3:
    print(parolilep(int(input()),int(input()),int(input())))
elif a == 4:
    print(pramoug(int(input()),int(input())))

