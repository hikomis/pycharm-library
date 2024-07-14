from random import *
from Army import *
from countries import *
def loose(a,b):
    if a.army.power >= b.army.power * 3 or bankrupt(b) == False:
        print(f'Страна {b.name} проиграла')
        b.isExists = False
        addNews(f'Страна {b.name} проиграла стране {a.name}')
        randomNews()
        print(f'Страна просуществовала {b.age} лет')
        a.civilian += b.civilian * 0.7
        a.budget += b.budget * 0.5
        a.inWar = False
        b.inWar = False
        b = None
        return True
    elif b.army.power >= a.army.power * 3 or bankrupt(a) == False:
        print(f'Страна {a.name} проиграла')
        a.isExists = False
        addNews(f'Страна {a.name} проиграла стране {b.name}')
        randomNews()
        print(f'Страна просуществовала {a.age} лет')
        b.civilian += a.civilian * 0.7
        b.budget += a.budget * 0.5
        b.inWar = False
        a.inWar = False
        return False
    else:
        print('Война продолжается')
        randomNews()
        pass
def bankrupt(a):
    taxes = a.taxesShow()
    army = a.armySpentShow()
    if taxes < army:
        a.budget -= (army - taxes)
        if a.budget < 0:
            return False
        else:
            addNews(f'Затраты страны {a.name} на армию превысили допустимые траты')
            randomNews()
    return True

countries = []

country1 = Country('Ru', 245, 70000000, 65000, None, 20000000000, 248000)
country1.isPlayer = True
army1 = Army(country1, 100000, 20000, 15, 10, 5, 8, 20, 0)
country1.setArmy(army1)
countries.append(country1)

country2 = Country('Russia', 245, 70000000, 65000, None, 20000000000, 248000)
army2 = Army(country2, 100000, 20000, 15, 10, 5, 8, 20, 0)
country2.setArmy(army2)
countries.append(country2)

country3 = Country('Austria', 245, 70000000, 65000, None, 20000000000, 248000)
army3 = Army(country3, 100000, 20000, 15, 10, 5, 8, 20, 0)
country3.setArmy(army3)
countries.append(country3)

country4 = Country('Spain', 245, 70000000, 65000, None, 20000000000, 248000)
army4 = Army(country4, 100000, 20000, 15, 10, 5, 8, 20, 0)
country4.setArmy(army4)
countries.append(country4)
def chooseCountry():
    for i in range(0,len(countries)):
        print(f'Страна №{i+1} --> {countries[i].name}')
    choice = int(input('Выберите за кого хотите играть: '))
    countries[choice-1].isPlayer = True
    return countries[choice-1]

def otherCountries():
    other = []
    for i in range(0,len(countries)):
        if countries[i].isPlayer == False:
            other.append(countries[i])
    return other

def theStateOfWAr():
    for i in otherCountries():
        if i.inWar == True:
            print(f'Страна{i.name} в состоянии войны')
        else:
            print(f'Страна{i.name} ни с кем не воюет')


def DeclarationWar(my,other):
    for i in range(len(other)):
        shans = randint(1,100)
        if shans in range(1,13) and my.inWar == False:
            other[i].declareWar(my)
            addNews(f'Страна {other.name} объявила войну {my.name}')
            randomNews()
            return other[i]
        else:
            continue
    return None

def showOtherCountries(other):
    for i in range(0,len(other)):
        print(f'Страна №{i + 1} --> {other[i].name}')

def fight(power1,power2):
    k = 0
    while power1 > 0 and power2 > 0:
        t = randint(1,2)
        if t == 1:
            power1 -= 1
        else:
            power2 -= 1
        k += 1
        if k == 10000:
            k = 0
            print(f'У вас осталось {power1} мощи,а у врага осталось {power2} мощи')
    if power2 == 0:
        print('Вы одержали победу в данном бою')
        addNews(f'Наши войска разгромили врага на поле боя ')
        randomNews()
        return True
    else:
        print('Вы потерпели поражение в данном бою')
        addNews(f'Наши командующие армией приняли решение о тактическом отступлении ')
        randomNews()
        return False
def mobilision(yourCountry):
    if yourCountry.isPlayer == True:
        people = int(input('Введите количество людей которых хотите мобилизовать: '))
        yourCountry.mobilization(people)
        addNews(f'В Стране {yourCountry.name} мобилизировавли {people} человек')
        randomNews()
    else:
        if yourCountry.army.power <= yourCountry.civilian * 0.15:
            people = randint(int(yourCountry.civilian * 0.08),int(yourCountry.civilian * 0.22))
            yourCountry.mobilization(people)
            addNews(f'В Стране {yourCountry.name} мобилизировавли {people} человек')
            randomNews()
        else:
            pass




def clearNews():
    news.clear()
ready_news = ['Проведены исследования: Оказалось, что смартфоны превращают людей в растения!',
              'Взрыв на фабрике в Китае: погибли десятки рабочих, эвакуировано более 100 человек',
              'Президент США объявил о новых санкциях против России в связи с кибератакой на американские компании',
              'Удивительное открытие: Ученые нашли способ добывать электроэнергию из пирожных!',
              'Искусственный интеллект стал лучшим певцом мира, обойдя Тейлор Свифт и Би Би Кинга!',
              'Взрывоопасные капустные растения угрожают миру: зеленые овощи взорвались после землетрясения в овощном складе!',
              'Космическое агентство NASA объявило о новом проекте по колонизации Луны!',
              'Исследователи обнаружили новый вид динозавра в южной Африке.',
              'Вчерашний дождь оказался ошибкой метеорологов – они забыли включить фильтр для запускающихся котов.',
              'Местная кошка поселилась в мэрии и начала предлагать законы о больших шерстяных шариках на заседаниях',
              'Местный новый герой участвовал в розыгрыше лотереи и выиграл 100 килограммов котят.',
              'В Центре здоровья открылась специальная тренажерная комната для домашних питомцев – "Фитнес для лап',
              'Ученые обнаружили планету, на которой возможна жизнь из пластика',
              'Врачи разработали новый препарат, который делает человека невидимым',
              'Искусственный интеллект разработал способ увеличения IQ человека до 300',
              'Антигравитационное устройство (летающая машина) было изобретено японскими ученым',
              'Археологи нашли главного артефакта пирамиды: древнюю карту с описанием обитаемой планеты в другой галактике',
              'Пророчество сбылось: небо загорелось фиолетовым и зарождается новая эра',
              'Пушистые монстры из глубин океана вторглись на пляжи и начали нападать на людей',
              'Новое открытие: ученые разработали лекарство, способное остановить процесс старения на 10 лет',
              'Мистическое явление: Китайский Великий Китайский Мур, ставший памятником культуры, внезапно исчез и появился в Америке',
              ]
news = []
def showNews():
    print('NEWS:')
    for i in news:
        print(i)

def addNews(text):
    news.append(text)


def randomNews():
    s = randint(1,8)
    if s == 1:
        addNews(ready_news[randint(0,20)])






