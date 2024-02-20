#정수를 입력 받아서 홀수인지 짝수인지 판별하여 출력
'''
num = int(input('정수 입력 : '))
rest = num % 2
if rest == 0:
    print('짝수')
else:
    print('홀수')

#정수 3개를 입력 받아서 제일 큰 수 출력

#제출:

inum1 = int(input('정수1 입력 :'))
inum2 = int(input('정수2 입력 :'))
inum3 = int(input('정수3 입력 :'))

if inum2 >= inum3:
    if inum1 >= inum2:
        largest = inum1
    else:
        largest = inum2
else:
    if inum3 >= inum3:
            largest = inum3
    else:
            largest = inum1
print('제일 큰 수 :',largest)

            


#답안:

inum1 = int(input('정수1 입력 :'))
inum2 = int(input('정수2 입력 :'))
inum3 = int(input('정수3 입력 :'))

if inum1>=inum2 and inum1 >= inum3:
    largest = inum1
elif inum2>=inum1 and inum2 >= inum3:
    largest = inum2
else:
    largest = inum3

print('제일 큰 수 :',largest)



#Student1


inum1 = int(input('정수1 입력 :'))
inum2 = int(input('정수2 입력 :'))
inum3 = int(input('정수3 입력 :'))
if inum1>=inum2:
    max=inum1
else: max=inum2

if max>=inum3:
    pass
else: max=inum3

print('제일 큰 수 :',max)



#도형을 선택해서 면적을 구하기

figure = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : '))

if figure == 1 or figure == 2 or figure == 3:
    if figure == 1:
        width = int(input('가로 입력 : '))
        height = int(input('세로 입력 : '))
        area = width * height
        figure_name = '사각형'
    elif figure == 2:
        width = int(input('밑변 입력 : '))
        height = int(input('높이 입력 : '))
        area = width * height * (1/2)
        figure_name = '삼각형'
    else:
        figure == 3
        radius = int(input('반지름 입력 : '))
        area = 3.141592 * radius * radius
        figure_name = '원'
    print(f'{figure_name}의 면적 = {area:.2f}')
else:
    print('입력 오류')


 '''

#주사위 눈 입력해서 컴퓨터와 대결 - randint() 사용

from random import randint
import time

mydice = int(input('주사위 눈의 수 입력 :'))
aidice = randint(1,6)
print('당신의 숫자는 ',mydice)
print('그리고 컴퓨터의 숫자는?')
time.sleep(2)
print('컴퓨터는 ',aidice)
print('========================')


if mydice > aidice:
    print('축하합니다. 이기셨습니다!')
elif mydice < aidice:
    print('컴퓨터가 이겼습니다!')
else:
    print('비겼습니다!')

    
                   


