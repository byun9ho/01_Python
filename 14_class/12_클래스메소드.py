# Class Method
# 인스턴스를 통하지 않고 클래스에서 바로 호출
# @classmethod를 지정하여 사용


class Person:
    count=0 #클래스변수

    def __init__(self):
        Person.count+=1

    @classmethod
    def print_count(cls): #cls: class를 의미
        print(f'{cls.count}명 태어났어요')

    @classmethod
    def create(cls): #생성자와 같은 메소드(Constructor)
        p=cls()
        return p

kim=Person()
Person.print_count()
choi=Person()
Person.print_count()

lee=Person.create() #클래스메소드로 인스턴스생성
Person.print_count()