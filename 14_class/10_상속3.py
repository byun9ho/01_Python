#다이아몬드상속: 다중상속의 한사례

class A:
    def greeting(self):
        print('Hello, this is A')

class B(A):
    def greeting(self):
        print('Hello, this is B')

class C(A):
    def greeting(self):
        print('Hello, this is C')

class D(B,C):
    pass

obj=D()
obj.greeting()

#서로 다른 클래스에서 동일한 이름의 메서드를 상속받는 경우 in 다이아몬드상속
# 메소드를 탐색하는 순서(MRO:Method Resolution Order)
# 클래스 다중 상속문의 왼쪽에서 오른쪽(즉, 먼저 나오는)

print(D.mro())

