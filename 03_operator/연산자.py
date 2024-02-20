# 연산자

#1. 산술연산자:

# divmod(x, y) : x를 y로 나눈 몫과 나머지 반환

# 문제1. 10000초는 몇분 몇초인가?

time = 10000
minutes = time // 60
seconds = time % 60
print(f'{time}은 {minutes}분 {seconds}초입니다')

time = 10000
hours = time // 3600 #minutes = time // 60
minutes = (time % 3600)//60 #hours = minutes // 60
seconds = (time % 3600)%60
print(f'{time}초는 {hours}시간 {minutes}분 {seconds}초입니다')


time = 10000
hours = time // 3600 #minutes = time // 60
time = time % 3600
minutes = (time)//60 #hours = minutes // 60
seconds = (time)%60
print(f'{time}초는 {hours}시간 {minutes}분 {seconds}초입니다')

# 연습문제 1: 현금이 5,000원, 사탕 가격이 120원, 최대한 사탕 몇개?

# 2. 관계연산자: > < >= <= == !=

a=100
b=5
result = a == b
print(f'{a}=={b}의 결과는 {result}')
print(f'{a}!={b}의 결과는 {a!=b}')
print(f'{a}>{b}의 결과는 {a>b}')



#3k. 논리연산자: and or not

print(a>10 and a<300)
print(not(a>200))

#4. 비트연산자: 논리곱&, 논리합|, ^ NOT ~ 시프트연산 << >>

print(f'~{a} : {~a}')
print(f'{b}<<1 : {b<<1}') #5를 왼쪽으로 쉬프트 한번(즉, 2를 곱한 것과 같음)
print(f'{b}<<3 : {b<<3}')
print(f'{b}>>2 : {b>>3}')
print(f'{b}<<3 : {b<<3}')
print(f'{a}>>3 : {a>>3}')

# 대괄호는 스트링 등에서 인덱스 가져오는

# 대입연산자: += -= *= /= //= %=

print('a=',a)
a+=10
print('a+=10', a)

#연습문제2 지폐교환프로그램 1,000원, 5000원, 10,000원, 50,000원으로 교환 및 나머지 계산

Mamt = int(input('교환할 금액을 원 단위로 입력하세요: '))
P50K = Mamt // 50000
P10K = (Mamt % 50000)//10000
P5K = ((Mamt % 50000)%10000)//5000
P1K = (((Mamt % 50000)%10000)%5000)//1000
Rest = Mamt - (P50K*50000 + P10K*10000 + P5K*5000 + P1K*1000)
print(f'입력한 {Mamt}원은 오만원권 {P50K}장, 만원권 {P10K}장, 오천원권 {P5K}장, 그리고 천원권 {P1K}장과 나머지 {Rest}원으로 교환합니다')

#money = int(input('입력할 지폐 : '))
#ftt, rest = divmod(money, 50000)
#ott, rest = divmod(rest, 10000)
#ft, rest = divmod(rest,5000)
#t, rest = divmod(rest,1000)
#print(f'50000원짜리 ==> {ftt}\n10000원짜리 ==> {ott}\n5000원짜리 ==> ' f'{ft}\n1000원짜리 ==> {t}\n' f'지폐로 바꾸지 못한 돈 ==> {rest}')

# 계산 횟수를 줄이기 위해서, 잔여금액 변수를 계속 사용. 복합대입(%=)을 사용해서 간결하게, 또는 divmod(Mamt, 50000)을 사용

Mamt = int(input('교환할 금액을 원 단위로 입력하세요: '))
P50K, Rest = divmod(Mamt, 50000)
P10K, Rest = divmod(Rest, 10000)
P5K, Rest = divmod(Rest, 5000)
P1K, Rest = divmod(Rest, 1000)
print(f'입력한 {Mamt}원은 오만원권 {P50K}장, 만원권 {P10K}장, 오천원권 {P5K}장, 그리고 천원권 {P1K}장과 나머지 {Rest}원으로 교환합니다')

Mamt = int(input('교환할 금액을 원 단위로 입력하세요: '))
P50K = Mamt//50000
Rest=Mamt
Rest%=50000
P10K = Rest//10000
Rest%=10000
P5K = Rest//5000
Rest%=5000
P1K = Rest//1000
Rest%=1000
print(f'입력한 {Mamt}원은 오만원권 {P50K}장, 만원권 {P10K}장, 오천원권 {P5K}장, 그리고 천원권 {P1K}장과 나머지 {Rest}원으로 교환합니다')


