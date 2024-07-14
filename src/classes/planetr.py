#КЛАСС
class Human():
    #КОНСТРУКТОР
    def __init__(self, name, sex, age=0):
    #АТРИБУТЫ --->
        self.name = name
        self.age = age
        self.sex = sex
        self.work = None

#МЕТОДЫ --->
    def hi(self):
        print(self.name + " say hello")


    def hiring(self,work):
        if self.age > 14:
            print("Now you are working " + work)
            self.work = work
        else:
            print("You are very young")
    def age(self):
        self.age += 1
        print("HAPPY BIRTHDAY, " + self.name + f"\nNow you are {self.age} years old")









human = Human("Artem","male",22)
human.age()
human.age()
human.age()
human.age()
human.age()
