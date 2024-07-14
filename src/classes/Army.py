from countries import *
class Rockets:
    def __init__(self,count=0):
        self.operator = False
        self.count = count
        self.price = 1300000000
class Army:
    def __init__(self,country,infantry,specops=0,tanks=0,fightJet=0,ships=0,heli=0,rockets=Rockets(),nuke=0):
        self.infantry = infantry
        self.tanks = tanks
        self.fightJet = fightJet
        self.ships = ships
        self.heli = heli
        self.rockets = rockets
        self.nuke = nuke
        self.specops = specops
        self.country = country
        self.power = self.infantry + self.tanks * 15 + self.fightJet * 74 + self.heli * 37 + self.rockets *190 + self.nuke * 400001 + self.ships * 7200 + self.specops*2
    def buyArmy(self):
        s = input('Что вы хотите купить?: \n1)танк\n2)корабль\n3)вертолёт\n4)ракеты\n5)ядерка\n6)самолёты боевые\n7)спецназ\n')
        count = int(input('Сколько вы хотите купить?: '))
        if s == '1':
            places = 5
            price = 300000000
            if self.country.budget >= count*price and self.infantry >= places*count:
                self.country.budget -= price
                self.infantry -= places*count
                self.power += count*10
                self.tanks += count
            else:
                print('Не хватает ресурсов')
        if s == '2':
            places = 1200
            price = 5500000000
            if self.country.budget >= count*price and self.infantry >= places*count:
                self.country.budget -= price
                self.infantry -= places * count
                self.power += count * 6000
                self.ships += count
            else:
                print('Не хватает ресурсов')
        if s == '3':
            places = 5
            price = 800000000
            if self.country.budget >= count * price and self.infantry >= places * count:
                self.country.budget -= price
                self.infantry -= places * count
                self.power += count * 32
                self.heli += count
            else:
                print('Не хватает ресурсов')
        if s == '4':
            if self.country.budget >= count * price and self.infantry >= places * count:
                self.country.budget -= price
                if self.rockets.operator == False:
                    self.infantry -= 10
                    self.power += 190*count
                    self.rockets.count += count
                    self.rockets.operator = True
                else:
                    self.power += 190 * count
                    self.rockets.count += count
            else:
                print('Не хватает ресурсов')
        if s == '5':
            places = 1
            price = 400000000000
            if self.country.budget >= count * price and self.infantry >= places * count:
                self.country.budget -= price
                self.infantry -= places * count
                self.power += count * 400000
                self.nuke += count
            else:
                print('Не хватает ресурсов')
        if s == '6':
            places = 2
            price = 1500000000
            if self.country.budget >= count * price and self.infantry >= places * count:
                self.country.budget -= price
                self.infantry -= places * count
                self.power += count * 72
                self.fightJet += count
            else:
                print('Не хвататет ресурсов')
        if s == '7':
            places = 1
            price = 15000000
            if self.country.budget >= count * price and self.infantry >= places * count:
                self.country.budget -= price
                self.infantry -= count
                self.power += count*1
                self.specops += count
            else:
                print('Не хватает ресурсов')

    def sellArmy(self):
        s = input('Что вы хотите продать?: 1)танк\n2)корабль\n3)вертолёт\n4)ракеты\n5)ядерка\n6)самолёты боевые\n7)спецназ\n')
        count = input('Что вы хотите продать?')
        if s == '1':
            if self.country.army.tanks >= count:
                self.country.budget += 150000000
                self.infantry += count*5
                self.power -= 15*count
            else:
                print('Танков нет')
        if s == '2':
            if self.country.army.ships >= count:
                self.country.budget += 2750000000
                self.infantry += count*1200
                self.power -= 6000*count
            else:
                print('Кораблей нет')
        if s == '3':
            if self.country.army.heli >= count:
                self.country.budget += 400000000
                self.infantry += count*2
                self.power -= 32*count
            else:
                print('вертолётов нет')
        if s == '4':
            if self.country.army.rockets >= count:
                self.country.budget +=650000000
                self.infantry +=0
                self.power -=100
            else:
                print('ракет нет')
        if s == '5':
            if self.country.army.nuke >= count:
                self.country.budget +=200000000000
                self.infantry += count
                self.power -= 400000*count
            else:
                print('ядерки нет')
        if s == '6':
                if self.country.army.fightJet >= count:
                    self.country.budget += 750000000
                    self.infantry += count * 2
                    self.power -= 72*count
                else:
                    print('самолётов нет')
        if s == '7':
            print('Невозможно продать')
    def showArmy(self):
        print(f'Ваша армия состоит из пехоты:{self.infantry}\nСпецназа:{self.specops}\nТанков:{self.tanks}\nКораблей:{self.ships}\nВеротлётов:{self.heli}\nСамолётов:{self.fightJet}\nРакет:{self.rockets}\nЯдерныхОрудий:{self.nuke}\nОбщая боевая мощь - {self.power}')

