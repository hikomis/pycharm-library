class planet():
    def __init__(self,gravity,name,atmospheric_pressure,age,oxygen):
        self.gravity = gravity
        self.name = name
        self.age = age
        self.atmospheric_pressure = atmospheric_pressure
        self.oxygen = 0
    def ttt(self,oxygen):
        if self.oxygen > 0:
            print('there is oxygen on the planet')
            self.oxygen = oxygen
        else:
            print('there is no oxygen')

    def rr(self):
        self.age += 1
        print("the planet has become older by one year " + self.name + f"\nnow the planet {self.age} years old")









planet1 = planet(1,"mars",760,22,4,)
planet2 = planet(33,"foritos",966,436,0)


if planet1.age > planet2.age:
    print(f"{planet1.name} старше")
else:
    print(f'{planet2.name} старше')

if planet2.gravity > planet1.gravity:
    f = planet2.gravity / planet1.gravity
    print(f'в {f} раз больше')

if planet1.oxygen > 0:
    print(f"жизнь на {planet1.name} возможна")
else:
    print(f'жизнь на {planet1.name} не возможна ')

if planet2.oxygen > 0:
    print(f'жизнь на {planet2.name} возможна ')
else:
    print(f'жизнь на {planet2.name} не возможна ')


