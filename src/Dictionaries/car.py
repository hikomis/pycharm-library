car = {}
count = int(input("Введите количество мест: "))
parkcar = 0
while True:
  ist = input().split(', ')
  if ist[0] == 'END':
      break
  elif parkcar < count and ist[0] == 'IN':
      car.update({ist[1]:parkcar})
      parkcar += 1
  elif ist[0] == 'OUT':
      car.pop(ist[1])
      parkcar -= 1
  else:
      print("нет мест")
for i in car.keys():
    print(i)