# Static Method 정적 메소드
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용하는 메소드
# 순수함수(pure function)
# @staticmethod 키워드사용. 메소드 위에 @staticmethod 정의.

class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def sub(a,b):
        print(a-b)

myCal=Calc()
myCal.add(10,20)
Calc.add(10,20) #바로 클래스의 메소드를 호출