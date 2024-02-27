# declare Car Class
# class 클래스이름[(상속클래스)]:
#       클래스변수(필드)선언 (예: 변수이름=0)
#       메서드 정의
#       def 메서드이름(self,매개변수):
#           기능구현코드

# 객체(인스턴스)생성
# 객체이름=클래스명() : 생성자
# 객체: 단독으로 객체만 지칭
# 인스턴스: 클래스와 연관지어서 부를때 사용

class Car:
    # pass
    color=''
    speed=0
    def drive(self):
        self.speed=10

# 인스턴스생성
car1=Car()   #Car(): 인스턴스 생성자함수
car2=Car()
car3=Car()

# 인스턴스의 필드 이용: 인스턴스이름.필드명
print(type(car1),id(car1))
print(type(car2),id(car2))
print(type(car3),id(car3))

#isinstance는 내장함수, 어떠한 클래스로부터 생성된 인스턴스인지 확인해 줌
print(isinstance(car1,Car)) #isinstance는 내장함수, 어떠한 클래스로부터 생성된 인스턴스인지 확인해 줌

# 메서드호출
car1.drive()
print(f'car1 speed: {car1.speed}') # car1.speed만 10으로 변경됨
print(f'car2 speed: {car2.speed}')
print(f'car3 speed: {car3.speed}')


#인스턴스생성후필드추가(그러나 보통은 클래스 만들때 정리)
# car1.color='red'
# car2.color='blue'
# car3.color='yellow'
# car1.speed=0
# car2.speed=0
# car3.speed=0
# print(car1.color)

#classes of python: int, float, str, set, dict, list, tuple -다... 클래스들
# a=int(10)
# print(a)
# b=list(range(10))
# print(b)
# c=dict(x=10,y=20)
# print(c)
#
# print(type(a),type(b),type(c))
# print(isinstance(a,int))
# print(isinstance(a,float))
# d=10.5
# print(isinstance(d,float))

