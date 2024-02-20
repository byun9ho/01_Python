'''
=============
#조건문

#if문 / ifelse문

num=int(input('정수입력 : '))
if num>10:
    print('10보다 크네요')
else: #콜론은 한칸띄고 써도 되고, 붙여도 됨
    print('10보다 작거나 같아요')

#pass

num=int(input('정수입력 : '))
if num>10:
    print('10보다 크네요')
else: 
    pass


#연습문제: ID 및 패스워드 비교

ID='flower'
PWD='1234'
KeyinID = input('아이디 입력:')
KeyinPWD = input('비밀번호 입력:')

if ID==KeyinID and PWD==KeyinPWD:
        print('로그인성공')
else: print('로그인실패')






#중첩 if: if조건이 만족하는 경우 또다른 조건에 따라 실행
#if아래 if가 존재 

ID='flower'
PWD='1234'
KeyinID = input('아이디 입력:')
KeyinPWD = input('비밀번호 입력:')

if ID==KeyinID:
    if PWD==KeyinPWD:
        print('로그인성공!')
    else: print('로그인실패! 비밀번호 오류') #pass
else: print('로그인실패! ID오류')



ID='flower'
PWD='1234'
KeyinID = input('아이디 입력:')
KeyinPWD = input('비밀번호 입력:')

if ID==KeyinID:
    if PWD==KeyinPWD:
        print('로그인성공!')
    else: print('로그인실패! 비밀번호 오류') #pass
else:
    if PWD==KeyinPWD:
        print('로그인실패! ID오류')
    else: print('로그인실패! ID와 비밀번호 오류') 


ID='flower'
PWD='1234'
KeyinID = input('아이디 입력:')
KeyinPWD = input('비밀번호 입력:')

if ID==KeyinID:
    if PWD==KeyinPWD:
        print('로그인성공!')
    else: print('로그인실패! 비밀번호 오류') #pass
elif PWD==KeyinPWD:
        print('로그인실패! ID오류')
else: print('로그인실패! ID와 비밀번호 오류')



# 점수(0~100) 받아서 학점 출력
# 90점 이상 A, 90미만 80점 이상 B, 80점 미만 70점 이상 C, 70점 미만 60점 이상 D, 60점 미만 F

score=int(input('점수를 입력하시오: '))
if score >= 90:
    print(f' 입력하신 점수 {score}에 따르면 학점은 A입니다')
elif score >=80:
    print(f' 입력하신 점수 {score}에 따르면 학점은 B입니다')
elif score >=70:
    print(f' 입력하신 점수 {score}에 따르면 학점은 C입니다')
elif score >=60:
                print(f' 입력하신 점수 {score}에 따르면 학점은 D입니다')
else: print(f' 입력하신 점수 {score}에 따르면 학점은 F입니다')


===================
'''

score=int(input('점수를 입력하시오: '))
#if score >= 90 and score <= 100:
if score < 0 or score > 100:
    break
    print('입력오류')
else:
    pass

if 90 <= score <= 100:
    grade='A'
elif 90 > score >=80:
    grade='B'
elif 80 > score >=70:
    grade='C'
elif 70 > score >=60:
    grade='D'
else:
    grade='F'

print(f' 입력하신 점수 {score}에 따르면 학점은 {grade}입니다')





