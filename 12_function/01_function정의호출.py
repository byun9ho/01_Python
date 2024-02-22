# 재사용/자주 사용하는 기능들을 위한 코드 집합
# 경제적, 관리용이,
# 내장함수(built-in), 사용자정의함수
# https://docs.python.org/3.12/library/functions.html#exec

# 함수 정의 및 호출

# print(Name, Age, Contact_Info)=show_info()
#
# def show_info():
#     print('이름 : 홍길동')
#     print('나이 : 20')
#     print('연락처 : 010-111-1111')
#
# def show_info1():
#     # name,age, contact_info input
#     name=input('이름입력 : ')
#     age=input('나이입력 : ')
#     phone=input('연락처입력 : ')
#     print(f'이름 : {name}')
#     print(f'나이 : {age}')
#     print(f'연락처 : {phone}')
#
#
# show_info()
#
# show_info1()

# 문제: 두 정수를 입력받아 더하고 그 결과를 출력하는 함수 add()정의하기

# def addvar(Num1,Num2):
#     #Num1=int(input('첫번째 정수를 입력하시오 : '))
#     #Num2=int(input('두번째 정수를 입력하시오 : '))
#     print(f'두 정수의 합은 = {Num1+Num2}')
#
# Num1 = int(input('첫번째 정수를 입력하시오 : '))
# Num2 = int(input('두번째 정수를 입력하시오 : '))
# addvar(Num1,Num2)

# def add():
#     Num1=int(input('첫번째 정수를 입력하시오 : '))
#     Num2=int(input('두번째 정수를 입력하시오 : '))
#     print(f'두 정수의 합은 = {Num1+Num2}')
#
# result=add()
# print(result)

# Def:Return Value of Function

def add2():
    num1 = int(input('첫번째 정수를 입력하시오 : '))
    num2 = int(input('두번째 정수를 입력하시오 : '))
    result=num1+num2
    print(f'두 정수 {num1}+{num2} 합은 = {result}')
    return result

print(f'return value = {add2()}')