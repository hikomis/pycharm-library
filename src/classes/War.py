from Army import *
from random import *
from countries import *
from WarInterface import *

yourCountry = chooseCountry()
otherCountries = otherCountries()

enemy = None

while True:
    for i in otherCountries:
        mobilision(i)
    if len(otherCountries) == 0:
        print('Вы получили мировое господство')
        break
    elif yourCountry.inWar == False:
        s = input('хотите ли вы объявить войну?: ')
        if s.lower() == 'да':
            showOtherCountries(otherCountries)
            count = int(input('на кого вы хотите напасть?: '))
            yourCountry.declareWar(otherCountries[count-1])
            addNews(f'Страна {yourCountry.name} объявила войну {otherCountries[count-1].name}')
            randomNews()
            enemy = otherCountries[count-1]
        else:
            enemy = DeclarationWar(yourCountry,otherCountries)
    elif yourCountry.inWar == True and enemy != None:
        enemyArmy = enemy.attack()
        yourCountryArmy = yourCountry.attack()
        if loose(yourCountry, enemy) == True:
            otherCountries.remove(enemy)
            continue
        elif loose(yourCountry,enemy) == False:
            print('Игра окончена ')
            break
        else:
            fight(yourCountryArmy,enemyArmy)
    for i in otherCountries:
        i.EndForTheYear()
    yourCountry.EndForTheYear()
    while True:
        s = int(input(f'Выберите какая ифнормация вас интересует?:\n1-рождамемость в вашей стране в год\n2-состоянии страны\n3-состоянии армии \n4-состояние войны между странанми\n5-узнать новости\n6-военный магазин\n7-провести мобилизация '))
        if s == 1:
            yourCountry.showBorn()
        elif s == 2:
            yourCountry.showCity()
        elif s == 3:
            yourCountry.army.showArmy()
        elif s == 4:
            theStateOfWAr()
        elif s == 5:
            showNews()
        elif s == 6:
            yourCountry.army.buyArmy()
        elif s == 7:
            mobilision(yourCountry)
        else:
            clearNews()
            break







