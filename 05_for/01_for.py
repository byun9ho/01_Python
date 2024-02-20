# 반복문 for
# 1에서 10까지의 정수 더하기
'''
# total = 1+2+3+4+5+6+7+8+9+10

total = 1+2+3+4+5+6+7+8+9+10
print(total)

total = 0
for num in range(1,11):
    total += num

print(total)

total = 0
for num in range(1,11,2):
    total += num

print(total)

total = 0
for num in range(2,11,2):
    total += num

print(total)

# 시작값 끝값을 받아 이 사이에 있는 정수 더하기

st = int(input('시작값 ='))
en = int(input('끝값 =')) +1
total = 0
for num in range(st,en):
    total += num

print(total)

#학생 예시코드

start,end = map(int,input().split()) # 단점 사용자가 무슨 값을 입력해야 하는지 알수 없음.
total=0
for num in range(start,end+1):
    total=+num

print(total)

'''

# 5명의 점수를 입력 받아 60이상 합격, 60미만 불합격

for _ in range(5):
    jumsu=int(input('0~100사이의 점수 입력: '))
    if jumsu >= 60:
        print(f'{jumsu} 합격')
    else:
        print(f'{jumsu} 불합격')

        
