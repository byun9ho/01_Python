# # 객체의 필요성
#
# # 더하기 기능을 위한 계산기 구현
# # 3+4+5+9
#
# result1=0
# result2=0
# def adder1(num):
#     global result1
#     result1+=num
#     return result1
# def adder2(num):
#     global result2
#     result2+=num
#     return result2
#
# print(adder1(3))
# print(adder2(7))
# print(adder1(9))

# def adder(num):
#     # result=0
#     global result
#     result+=num
#     return result
#
# print(adder(3))
# print(adder(7))
# print(adder(9))

# result=0
result=0
class AddCal:
    def __init__(self):
        self.result=0

    def adder(self,num):

        self.result+=num
        return self.result

# cal1=AddCal()
# cal2=AddCal()
#
#
# a3=cal1.adder(3)
# a7=cal2.adder(7)
#
# print(a3,a7)
#
# print(result)

myadder=AddCal()
myadder.adder(10)
print(myadder.result)
myadder1=AddCal()
myadder1.adder(20)
print(myadder1.result)
myadder2=AddCal()
myadder2.adder(30)
print(myadder2.result)
youradd=AddCal()
print(youradd.result)

youradd.adder(100)
print(youradd.result)
print(type(myadder))




