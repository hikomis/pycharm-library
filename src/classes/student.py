from random import choice
class SchoolHuman:
    def __init__(self, name,age,surname,sex,patronymic):
        self.name = name
        self.age = age
        self.surname = surname
        self.sex = sex
        self.patronymic = patronymic
class Teacher(SchoolHuman):
    def __init__(self,name,age,surname,sex,patronymic,subject,salary,experience):
        super().__init__(name=name,age=age,surname=surname,sex=sex,patronymic=patronymic)
        self.subject = subject
        self.salary = salary
        self.experience = experience
    def lesson(self):
        if self.subject == 'M':
            lesson = ['алгебры','геометрии']
            print(f'{self.name} ведёт урок {choice(lesson)}')
        elif self.subject == 'H':
            print(f'{self.name} ведёт урок истории')
        elif self.subject == 'R':
            lesson2 = ['Литературы','русского языка']
            print(f'{self.name} ведёт урок {choice(lesson2)}')
        elif self.subject == 'F':
            print(f'{self.name} ведёт физкультуру')
        else:
            print('ТЫ не учитель')
    def estimation(self,student,mark):
        print(f'{self.name} поставил {mark}, ученику {student.name} из {student.formNumber}{student.formLetter}')
class Student(SchoolHuman):
    def __init__(self,name,age,surname,sex,patronymic,formNumber,formLetter,isLargeFamily):
        super().__init__(name=name,age=age,surname=surname,sex=sex,patronymic=patronymic)
        self.formNumber = formNumber
        self.formLetter = formLetter
        self.isLargeFamily = isLargeFamily
class Worker(SchoolHuman):
    def __init__(self,name,age,surname,sex,patronymic,salary,typeOfWork):
        super().__init__(name=name, age=age, surname=surname, sex=sex, patronymic=patronymic)
        self.salary = salary
        self.typeOfWork = typeOfWork
    def working(self):
        if self.typeOfWork == 'O':
            print(f'{self.name} на рабочем месте')
        elif self.typeOfWork == 'Y':
            school = ['класс',"туалет","раздевалку","коридор","кладовку"]
            print(f'{self.name} убирает {choice(school)}')
        elif self.typeOfWork == 'S':
            print(f'{self.name} принтеры чинит')
        else:
            print("Кто ты?")

student = Student('Вася',18,'Пупкин','мужчина','Ильич','9','Г',False)
teacher  = Teacher('Антонина',32,'Иванова','Женский','Конастантиновна','M',45000,3)
teacher.lesson()
teacher.estimation(student,3)




