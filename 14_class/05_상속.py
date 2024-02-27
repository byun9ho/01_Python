# 상속:부모클래스로부터 상속받은 필드와 메소드를 이용하거나 추가변경하여 활용(재사용)
# 메소드재정의(method override)

class Car(object):
    def __init__(self,speed=0,color=''):
        self.speed=speed
        self.color=color

    def drive(self):
        print(f'{self.speed}로 주행한다.')

class Truck(Car):
    def __init__(self,speed,color,load):
        super().__init__(speed,color)
        self.load=load

    # 메소드 재정의
    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행한다.')

    def loading(self):
        print(f'최대 {self.load}양의 짐을 운반할 수 있는 트럭')

car1=Car()
truck1=Truck(0,'blue',5)
truck2=Truck(0,'white',10)
truck3=Truck(0,'blue',5)
for car in [car1,truck1,truck2,truck3]:
    car.drive() # 같은 이름의 메소드(drive) 다만 자동차와 트럭은 살짝 다르게 기능/오버라이드

# car1.drive()
# truck1.drive()


