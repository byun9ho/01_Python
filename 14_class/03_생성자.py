# 생성자(constructor)
# 형식: def __init__(self, *args):
#           필드초기화

# __메서드명__(): 예약함수

# 비공개필드와 메서드: 정보은닉(encapsulation)
# __변수명:비공개필드 > 클래스내부에서만 사용
# 비공개필드는 접근 가능한 메서드를 정의하여 사용
# __메서드명() > 비공개메서드 클래스내부에서만 사용
# 접근 가능한 또다른 메서드를 통해 접근

class Car:
    # def __init__(self, color,model,date): # 생성자 __가 붙어 있으면 (비공개 외에도) 미리 예약된 것을 의미함.
    def __init__(self,color,date,modelN,model='BMW'): #생성자 / 디폴트로 BMW.제일 마지막에 디폴트들
        # self.color='black'
        self.color=color #보통 필드와 매개변수 이름 같이 씀
        self.speed=0
        self.modelN=modelN
        self.model=model
        self.__date=date #비공개필드 비공개

    def __modelN(self):
        return self.modelN

    def drive(self):
        self.speed=10

    def print_date(self):
        print('Manufactured Date is ',self.__date) #비공개필드는 변수내부에서만 사용. 이렇게 내부에서 메소드를 만들어서 접근

    def print_info(self):
        print('VIN Number: ',self.modelN)
        print('Vehicle Color: ',self.color)
        print('Vehicle Model :',self.model)
        self.print_date()

# car1=Car()
car1=Car('red','2024-01-01','KMH2123252','BMW',)
# car2=Car()
car2=Car('black','2020-01-30','WBH298999','Nexo') #생성자에서 정의된 변수를 넣어서 인스턴스를 만들어야 함(아니면 에러)
car3=Car('black','2021-12-30','5W1H')


print('car1 color : ',car1.color)
print('car2 color : ',car2.color)
print('car1 model : ',car1.model)
# print(car1.__date) #비공개필드는 직접 사용불가능. 다른 메소드에 의해 사용가능
# car1.print_date()
print('car3 model : ',car3.model)

car1.print_info()