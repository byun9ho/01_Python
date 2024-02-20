# day1 : 변수에 대해서 실습

# 실습1: 두 변수의 값 교환(swap)

#1 방법1 : 고전적 방식

'''
a=10
b=5
print(a, b)

c=a
a=b
b=c
print(a, b)


# 방법2 : 파이썬 방식

a, b = 10, 5
print('a=', a, 'b=', b)
a, b=b, a
print('a=', a, 'b=', b)

# 실습2 : 변수 삭제
#del a
#print(a)

# 실습3 : 변수의 값 출력 print()
age=30
name='HongGilDong'
print(name, age)

addr='서울시 서초구'
result = name + "은 " + addr + '에 살아요'
print(result)

print(name + ": 나이는 " +str(age) + ' 입니다')
#TypeError: 문자열과 숫자는 연결할 수 없다.
#숫자를 문자열로 변환하는 함수 활용: str( 숫자)

# 실습4 : 변수를 이용한 계산 결과값 출력
# 삼각형의 넓이 계산

w = 7
h = 5
s = ( w * h ) / 2
print('넓이=', s)

# print() 함수의 다양한 출력
# print('문자열', 변수)
# print('서식' %값 )
print('넓이=%d' %s)

#문자제어열 format string code: %f, %d, %s, %c, %x. "%o (float, decimal, string, character, hex(16 digit), oct(8 digit)

#방법1: '서식' % 값

result = '%s은 %s에 살고 나이는 %d에요' %(name, addr, age)
result2 = '넓이=%.2f' %s
pcnt = 10.5
result3 = '전체면적의 %f%%입니다' % pcnt
print(result)
print(result2)
print(result3)

#방법2: format() 함수

#format(숫자, '숫자서식')

#result4= format(s, '.2f')
#print(result4)
#print(format(100, '5d'))

#연습문제
#다음의 변수 값들을 이용하여 총점과 평균을 계산해서 예시와 같이 출력하기

#kor = 90
#eng = 80
#math = 75

#총점: 245, 평균: 81.66

'''

kor=90
eng=80
math=75
total = kor + eng + math
avg =  (total / 3)
print('총점: ', total, ', 평균: ', format(avg, '5.2f'), sep=' ')
print('총점: %d,   평균: %.2f' %(total, avg))
#print('총점: %d,평균: %5.2f', %(total,avg))

# .py로 되어 있는 파일을 모듈이라고 부










