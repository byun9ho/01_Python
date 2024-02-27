class Dog:
    dog_id=0
    def __init__(self,name='',breed='',size='',age='',color=''):
        self.name=name
        self.breed=breed
        self.size=size
        self.age=age
        self.color=color
        # self.dog_id = self.dog_id+1
        Dog.dog_id=Dog.dog_id+1
    def eat(self,food):
            print(f'{self.name}이(가) {food}를 먹는다')
    def sleep(self):
            print(f'{self.name}이(가) 잠잔다')

    def sit(self):
            print(f'{self.name}이(가) 앉아있다')

    def run(self):
            print(f'{self.name}이(가) 달린다')

    def __repr__(self):
        return f'{self.name}의 품종은 {self.breed}, 나이: {self.age}'


dog1=Dog('삐삐','Maltese','small',2,'white')
print('dog1의 id',dog1.dog_id)
print(dog1)

dog2=Dog('벤','Chow Chhow','medium',3,'brown')
print('dog2의 id',dog2.dog_id)

dog3=Dog('뭉치','Mastiff','large',5,'black')
print('dog3의 id',dog3.dog_id)

dog1.eat('foods')
dog2.sleep()
dog3.sit()
dog1.run()

dog4=Dog()
print('dog4의 id',dog4.dog_id)

# print(Dog.dog_id)
# print(Dog().dog_id)

print(dog1)
print(dog2)

result=''
result=dog1 #dog1만 호출해도 __repr__ 함수가 불림
print(result)

# print(dog1.dog_id) # dog1에 선언해 주지 않아도 모두 dog_id를 가지고 있음.
# print(dog2.dog_id)
# print(dog3.dog_id)

#인스턴스변수: 인스턴스가 소유하고 있는 변수
#클래스변수: 전역변수와 같이 클래스의 모든 인스턴스들이 공유하는 변수(또는 attribute)
#클래스이름.클래스변수명으로 메서드 내부에서 사용하고
#인스턴스이름.클래스변수명으로 사용(밖에서)

