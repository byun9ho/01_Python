# class Terran(object):
#     def __init__ (self, mineral):
#         self.scv = 4
#         self.marine = 0
#         self.medic = 0
#         self.mineral = mineral
#     def command(self, SCV=False):
#         self.mineral += 8*self.scv
#         if SCV:
#             self.scv += 1
#             self.mineral -= 10
#     def barrack(self, Marine=False, Medic=False):
#         self.mineral += 8*self.scv
#         if Marine:
#             self.marine += 1
#             self.mineral -= 15
#         if Medic:
#             self.medic += 1
#             self.mineral -= 25
#     def check_source(self):
#         print("Mineral: "+str(self.mineral))
#
# User = Terran(50)
# User.command(True)
# User.barrack(True,True)
# User.check_source()

# class Score:
#     def __init__ (self,student):
#         tmp = student.split(",")
#         self.name = tmp[0]
#         self.midterm = int(tmp[1])
#         self.final = int(tmp[2])
#         self.assignment = int(tmp[3])
#         self.score = None
#         self.grade = None
#     def total_score(self):
#         test_score = ((self.midterm + self.final)/2)*0.8
#         if self.assignment>=3:
#             assign_score = 20
#         elif self.assignment>=2:
#             assign_score = 10
#         elif self.assignment>=1:
#             assign_score = 5
#         else:
#             assign_score = 0
#             self.score = test_score + assign_score
#     def total_grade(self):
#         if self.assignment==0:
#             grade = "F"
#         elif self.score >=90:
#             grade = "A"
#         elif self.score >=70:
#             grade = "B"
#         elif self.score >=60:
#             grade = "C"
#         else:
#             grade = "F"
#         self.grade = grade
#         return grade
#
# student_john = Score("john,90,90,0")
# aa = student_john.total_score()
# bb = student_john.total_grade()
# print(aa,bb,student_john.score,student_john.grade)
#
# class Person:
#     def __init__(self,name,age,position):
#         self.Name=name
#         self.Age=age
#         self.Position=position
#     def show_info(self):
#         print('Name : {}'.format(self.Name))
#         print('Age  : {}'.format(self.Age))
#         print('Position: {}'.format(self.Position))
#         print("I'm {0} {1}. My age is {2}".format(self.Position,self.Name,self.Age))
#
# class Researcher(Person):
#     def __init__(self,name,age,position,degree):
#         Person.__init__(self,name,age, position)
#         self.Degree=degree
#     def show_info(self):
#         Person.show_info(self)
#         print("I'm {}.".format(self.Degree))
#
# if __name__ == '__main__':
#     researcher_john=Researcher("John","22","Researcher","Bachelor of Science")
#     researcher_tedd=Researcher("Tedd","40","Head of Inst.","Ph.D")
#     researcher_john.show_info()
#     print("="*50)
#     researcher_tedd.show_info()
#
class TV(object):
    def __init__(self,size,year,company):
        self.size=size
        self.year=year
        self.company=company
    def describe(self):
        print(self.company+"에서 만든 "+self.year + "년형" + self.size+"인치"+"TV")

class Laptop(TV):
    def __init__(self,size,year,company):
        self.size=size
        self.year=year
        self.company=company
    def describe(self):
        print(self.company+"에서 만든 "+self.year + "년형" + self.size+"인치"+"노트북")

LG_TV=TV("32","2019","LG")
LG_TV.describe()

samsung_microwave=Laptop("15","2018","Samsung")
# print(samsung_microwave.company,samsung_microwave.size,"inch - MY: ",samsung_microwave.year,"year model")