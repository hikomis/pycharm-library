import random as r
def luck():
    num = r.randint(1,25)
    if num in [1,2]:
        print('Вы заболели и остаётесь дома')
        return 0
    elif num in [3,5,6]:
        a = r.randint(1,50)
        money = 100 * a
        print("Вы нашли кошелёк с деньгами,в нём было",money,"рублей")
        return money
    elif num in [7,8]:
        print("Вы сломали руку, остаётесь дома")
        d = r.randint(1,3)
        if d == 1:
            print("у вас была страховка вам выплатили 6000")
            return 6000
        else:
            print("у вас нет страховки, выплатите 5000")
            return -5000
    elif num in range(9,21):
        print("День прошёл спокойно")
        return 0
    elif num in [21]:
        print("Вы сбили пешехода,вы оплачиваете его лечение")
        return -12000
    else:
        print("Вы хорошо поработали")
        return 2400


def kasino():
    num = r.randint(1,2)
    if num in [1]:
        a = int(input("Введите сумму: "))
        money = 2 * a
        print("Вы виграли")
        return money
    else:
        b = int(input("Введите сумму: "))
        print("вы проиграли")
        return -b

def kaz():
    num = r.randint(1,6)
    b = int(input("Введите число которое выпадет: "))
    if num == b:
        a = int(input("Введите ставку: "))
        money = 6 * a
        print("Вы виграли")
        return money
    else:
        b = int(input("Введите сумму: "))
        print("вы проиграли")
        return -b

def bar():
    num = r.randint(1,6)
    if num == 1:
        summa = r.randint(500,5000)
        print("У вас стащили деньги")
        return - summa
    else:
        print("Вы хорошо отдохнули")
        return 0

def dosug():
    print("Вы просидели весь день дома")
    return 0