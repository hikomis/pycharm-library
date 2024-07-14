diction = {}
number_1 = int(input())
for i in range(0,number_1):
    strana = input("Введите страну: ").split()
    t = []
    t.extend(strana[1:len(strana)])
    diction.update({strana[0]:t})
goroda = int(input("Введите города: "))
for y in range(0,goroda):
    gor = (input("Введите город: "))
    for i in diction.keys():
      if gor in diction.get(i):
          print(i)