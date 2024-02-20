'''#Day 2
#기본자료형: int, float, bool, str
#iterative / 집합적 자료 / sequence형 자료: 리스트, 딕셔너리, 튜플, 세트

#2진수, 8진수, 16진수, 10진수
#hex(), hex(), hex()

print('bin(123)=', bin(123))
print('bin(0o123)=',bin(0o123))
print('bin(0x123)=',bin(0x123))

print('oct(123)=', oct(123))
print('oct(0b11010111)=',oct(0b11010111))
print('oct(0x123)=',oct(0x123))

print('hex(123)=', hex(123))
print('hex(0b11010111)=',hex(0b11010111))
print('hex(0o123)=',hex(0o123))

# 2) 형변환
# int(string), float(string), str(number)

# inst(string, base=10)
# int(string) : 10진수 기본
# int(string, 2) 2진수, int(string, 8) 8진수, int(string, base=16) 16진수

print("int('123')=",int('123'))
print('int(\'1010\', 2)=',int('1010', base=2))
print("int('ff',16)=", int('ff', 16))
print('int(\'123\',8=)',int('123',8))



#에러: NameError, TypeError, ValueError

#Value Error > print("int('ff')=",int('ff'))

#float(string) :문자열을 실수 형으로 변환

print('float("13.5")=',float('13.5'))
print('float("13")=',float('13'))

# str(숫자) : 문자열 변환

#print('나이는 = %d' % '20' ) TypeError
print('나이는 = %d' % int('20'))
#print('나이는 =' + 20 ) TypeError
print('나이는 = ' + str(20))

#input() 함수 : 키보드로 입력 받아서 문자열로 반환
#input(prompt) : prompt는 화면에 표시되는 문자열
name = input('이름은:')
year = int(input('출생연도는:'))
print(f'이름은 {name}, 나이는 {2024-year}')

num = input('실수입력: ')
result = int(num) * 10
print(f'{num}*10 = {result}')



# 연산자: *, +
# 문자열 + 문자열 = 두문자열을 연결, 더하기는 문자열과 숫자열을 연결해 주지 않는다
# 문자열 * 숫자 = 문자열을 숫자만큼 생성해서 연결 
# 실수로 입력된 문자열을 "정수"로 변환하면 valueError

# 문제1, 두 정수를 입력 받아서 합계 출력

Inum1=int(input('정수1 입력: '))
Inum2=int(input('정수2 입력: '))
print('합계는 ', Inum1+Inum2)

# 문제2. 몸무게와 키 값을 입력받아서 BMI 지수 계산

Weight = float(input('몸무게(킬로그램): '))
Height = float(input('키(센티미터): '))/100
BMI = float(Weight/(Height**2))
print(f'BMI는 {BMI:.2f}')
### print('BMI는 %f.2', BMI)
'''
a,b=map(int, input('num').split())
print(a+b)



