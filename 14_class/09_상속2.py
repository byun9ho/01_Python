#다중상속: 여러 클래스에서 상속받음

class Person:
    def __init__(self,name='',age=0):
        self.name=name
        self.age=age
    def greeting(self):
        print(f'{self.name} : Greetings!')

class Student(Person):
    def __init__(self,name='',age=0,stdid='',department='',grade=''):
        super().__init__(name,age)
        self.stdid=stdid

    def study(self):
        print(f'{self.name} study(studies)')

class University:
    def __init__(self,department='',grade=''):
        self.department=department
        self.grade=grade

    def manageScore(self):
        print(f'Study for {self.department}')

class Undergraduate(Student,University):
    pass

lee=Person(name='Lee')
kim=Student(name='Kim')
lee.greeting()
kim.greeting()
kim.study()
choi=Undergraduate(name='Choi')
choi.study()