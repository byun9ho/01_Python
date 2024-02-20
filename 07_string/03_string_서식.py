#
text1='Python is great!'
text2="Yes, it is."
text3 = "It's not like any other"  # 'It's not like any other' 2번째 어포스트로피 이후 명령어로 인식
text4='Don\'t walk.'
text5='This \n is \
        contain \
        temp'
print(text5)
text6='''apple
banana
melon
'''
print(text6)

#2 문자열 포맷지정
# 1) 포맷코드 '문자열 포맷코드' %(변수들)
# '%05d %.2f %s %c ' % ( )
print('%s는 %d살 입니다' %('홍길동',10))

# 2) '문자열 {위치인덱스}'.format(변수)
# ' {0:.2f} {2:5d} {1:s} '.format( , , )
name='kim'
age=10
print('{0}은 {1}살입니다'.format(name,age))

# '문자열 {변수}'.format(변수=값)

print('{name}은 {age}살입니다'.format(name='홍길동',age=10))
# format(변수, '서식') :
# format(bmi, '.2f')
#4) f'string: f'{변수} {변수:서식}'
print(f'{name}은 {age}살입니다.')

#4. 날짜 출력 포맷
# 주민번호 / 전화번호 / 우편번호 / 시간 / 날짜 /  : 코드화 되어 있어 숫자로 보이지만, 문자열로 사용

# 모듈 : 함수나 변수를 모아 놓은 파일
from datetime import date, datetime, timedelta # datetime 모듈

today= date.today()
print(today,type(today))
print(f'{today.year}년 {today.month}월 {today.day}일')
print(type(today.year))
#method: 메서드(객체 안에서 정의해서 쓰는 함수) field:객체의 변수

curr_time=datetime.now().time()
print(curr_time,type(curr_time))
print(curr_time.hour, curr_time.minute, curr_time.second, curr_time.microsecond)

print(timedelta(days=1))

print(timedelta(weeks=-1))
print(timedelta(days=-1))
print(timedelta(hours=-1))

print(today+timedelta(days=-1)) # 하루전
print(today+timedelta(weeks=1)) # 1주일 후
print(today+timedelta(hours=-1)) # 한시간 전(아마 오후 11시)

curr_datetime=datetime.now()
print(curr_datetime+timedelta(hours=-1))
print(curr_datetime+timedelta(days=2, hours=4))

print(today.strftime('%Y-%m-%d %H:%M:%S')) # style format time
print(today.strftime('%y-%m-%d %I:%M:%S %p'))
print(curr_datetime.strftime('%y년%m월%d일 %H:%M:%S'))

#4. 문자열 정렬
# 왼쪽정렬: <
# 오른쪽정렬: >
# 가운데정렬: ^
# 공백문자지정: -

text='Python is great!'

print('{0:<20}'.format(text), 'end')
print(f'{text:>20}')
print('{0:^20}'.format(text), 'end')
print(f'{text:^20}')

print('{0:#<20}'.format(text), 'end')
print(f'{text:*>20}')
print('{0:*^20}'.format(text), 'end')
print(f'{text:^20}')

