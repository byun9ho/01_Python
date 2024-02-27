# 예제: Line 클래스

# 특수메소드
# <https://docs.python.org/3/reference/datamodel.html#object.__del__>
class Line:
    def __init__(self,length): #생성자 Constructor
        self.length=length
        print(f'{self.length} 길이의 선이 생성 되었습니다.') #생성과정에 print를 넣으면 인스턴스생길때 프린트됨.

    # def __del__(self): #소멸자. garbage collection. 다 쓴거 같으면 알아서 제거
    #     print(f'{self.length} 길이의 선이 삭제 되었습니다.')

    # def __repr__(self):
    #     return f'선의 길이 : {self.length}인 선분'

    def __str__(self):
        return f'선분 {self.length}'

    def __add__(self,other):
        return self.length + other.length

    def __sub__(self,other):
        return self.length - other.length

    def __lt__(self, other): #less than
        return self.length < other.length

    def __gt__(self, other): #greater than
        return self.length > other.length

    def __le__(self, other): #less or equal
        return self.length <= other.length

    def __ge__(self, other): #great or equal
        return self.length >=other.length

    def __eq__(self, other):
        return self.length=other.length #True냐 False냐?

    def __ne__(self,other):
        return self.length != other.length

line1=Line(10)
line2=Line(20)

# del(line1)
# # print(id(line1))
# print(id(line2))

print(line1)
print(line2)
print(line1 + line2)
print(line1 - line2)
print(line1 >= line2)

#객체 자체에서 연산기호를 쓰기 위해 특별한 것들을 정의(클래스 오브젝트에서 정의)
# 그냥 클래스를 만들면 오브젝트(class object)에서 상속받음.