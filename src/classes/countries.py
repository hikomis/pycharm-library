from random import *
from Army import *
class Country:
    def __init__(self,name,age,civilian,salary,army,budget,territory,inWar=False,isExists=True,isPlayer=False):
        self.name = name
        self.age = age
        self.civilian = civilian
        self.army = army
        self.budget = budget
        self.territory = territory
        self.isPlayer = isPlayer
        self.inWar = inWar
        self.salary = salary
        self.isExists = isExists
    def taxes(self):
        self.budget += self.salary * 0.1 * 12 * self.civilian
        if self.isPlayer == True:
            print(f'В этом году в бюджет поступило {self.salary * 0.1 * 12 * self.civilian}₣')
        else:
            pass

    def taxesShow(self):
        return self.salary * 0.1 * 12 * self.civilian

    def armySpent(self):
        self.budget -= self.salary * 12 * self.army.power * 2.5

    def armySpentShow(self):
        return self.salary * 12 * self.army.power * 2.5

    def declareWar(self,country):
        if country.inWar == True:
            print('Эта страна уже воюет')
            pass
        else:
            if country.isPlayer == True:
                print(f'Вам объявила войну {self.name}')
            else:
                print(f'Вы объявили войну {country.name}')
            country.inWar = True
            self.inWar = True
            pass
    def mobilization(self,people):
        if self.civilian >= people:
            if self.isPlayer == True:
                print(f'Вы пополнили ряды на {people} человек')
            self.army.infantry += people
            self.civilian -= people
            self.army.power += people
            pass
        else:
            print('Такого количества людей нет')
            pass
    def setArmy(self,army):
        self.army = army
    def showCity(self):
        print(f'В вашей стране под названием {self.name} проживат: {self.civilian} человек\nБюджет страны:{self.budget}\nВозраст страны:{self.age}\nТерритория страны:{self.territory}')

    def born(self,):
        self.showBorn()
        self.civilian += self.civilian * 0.011

    def showBorn(self):
        if self.isPlayer == True:
            print(f'За год в стране родилось: {self.civilian * 0.011} человек')
        else:
            pass

    def getAge(self):
        self.age += 1
        if self.isPlayer == True:
            print(f"Ваша страна {self.name} стала старше на 1 год, её общий возраст {self.age}")
        else:
            pass

    def EndForTheYear(self):
        self.born()
        self.taxes()
        self.armySpent()
        self.getAge()
        if self.inWar == True and self.isPlayer == True:
            print('Страна в состоянии войны')
        elif self.inWar == False and self.isPlayer == True:
            print('Страна ни с кем не воюет')
        else:
            pass

    def attack(self):
        if self.isPlayer == True:
            s = int(input('сколько боевой мощи вы хотите отправить в бой?: '))
            if s <= self.army.power:
                self.army.power -= s
                return s
            else:
                print('не хватает войск')
                return self.attack()
        else:
            f = randint(1,5)
            n = self.army.power * 0.1 * f
            self.army.power -= n
            return round(n,0)











