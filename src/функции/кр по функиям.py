import luck
import time
import trip
budget = int(input("Введите свой бюджет: "))
zarplata = 1200
day = 0
while budget > 0:
    print('ДЕНЬ -',day)
    budget += luck.luck()
    time.sleep(5)
    budget = trip.day(budget) + zarplata
    print("у вас осталось - ", budget)
    time.sleep(5)
    day += 1
print("вы банкрот, вы прожили",day,"дней")

 # удача- заболел, нашёл деньги,сломал руку,обычный день,сбил кого то на пешеходнрм переходе,хорошее настроение.
 # может ли он сегодня работать
 # досуг- отдохнуть до завтра, зайди в онлайн казино, пойти в бар с друзьями, купить акции,сыграть в кости,

