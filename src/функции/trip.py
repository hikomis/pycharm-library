from luck import *
def day(a):
    vibor = int(input("Выберите то как вы хотите провести время\n1)остаться дома\n2)сходить в бар\n3)сыграть в монетку\n4)сыграть в кости\nвыбор - "))
    if vibor == 1:
        return a + dosug()
    elif vibor == 2:
        return a + bar()
    elif vibor == 3:
        return a + kasino()
    else:
        return a + kaz()
