a=[0,1,2,3,4]
print(a[:3],a[::-3])
print(a[::-1])

first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
print(order)
print(order[0][:-2])
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)

a=[1,2,3,4]
print(a*2)

a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']

a.append('g')
b.append(6)
print('g' in b, len(b))


# 실습문제
# 1)
blank=0
Mlist=list()
while blank==0:
    Mname=input('회원 입력 : ')
    if Mname is not "":
        Mlist.append(Mname)
    else:
        blank=1
#2)
stdttl=0
stdavg=0
stdcnt=0
stdnum=0
stdscore=list()
above80=0
stdnum=int(input('학생 수 입력 : '))
for stdcnt in range(stdnum):
    temp=int(input(f'학생 {stdcnt+1} 점수 입력 : '))
    stdttl=stdttl+temp
    stdscore.append(temp)
stdavg=stdttl/stdnum
# number of student with 80 points or above
for stdcnt in range(stdnum):
    if stdscore[stdcnt-1]>=80:
        above80+=1
    else:
        pass
print(f'총점 : {stdttl}')
print(f'평균 : {stdavg:.2f}')
print(f'80점 이상 학생 : {above80}명')

#3)
blank=0
prdlist=list()
while blank==0:
    prdname=input('상품 등록 (엔터키 누르면 종료) : ')
    if prdname != '':
        prdlist.append(prdname)
        print(prdlist)
    else:
        blank=1
print(f'등록된 상품 : ',*prdlist)

#4)
stdttl=0
stdavg=0
stdcnt=0
stdnum=0
stdscore=list()
above80=0
stdscoreasc=list()
stdnum=int(input('학생 수 입력 : '))
for stdcnt in range(stdnum):
    temp=int(input(f'학생 {stdcnt+1} 점수 입력 : '))
    stdttl=stdttl+temp
    stdscore.append(temp)
stdavg=stdttl/stdnum
# number of student with 80 points or above
for stdcnt in range(stdnum):
    if stdscore[stdcnt-1]>=80:
        above80+=1
    else:
        pass
stdscoredsc=sorted(stdscore,reverse=True)
print(f'총점 : {stdttl}')
print(f'평균 : {stdavg:.2f}')
print(f'80점 이상 학생 : {above80}명')
print(f'점수 내림차순 정렬 : {stdscoredsc}')

#5.
import random
idioms=['개과천선','구사일생','군계일학','무용지물','동고동락','유비무환','입신양명','괄목상대','막역지우','고장난명']
meaning=['잘못을 고치고 옳은 길에 들어섬','죽을 고비를 여러 번 겪으며 살아나다','평범한 사람 가운데 뛰어난 사람','아무짝에나 쓸모 없는 것','고통과 즐거움을 함께 한다','미리 준비해두면 근심 걱정이 없다','사회적으로 인정받고 출세하여 이름을 세상에 드날림','다른 사람의 학식이나 업적이 크게 진보한 것을 말함','생사를 같이 할 수 있는 친밀한 벗','상대 없이 혼자서는 어떤 일을 이룰 수 없다']
print('사자성어 맞추기 게임을 시작합니다.')
ans,mnum=0,0
while ans==0:
    mnum=random.randint(0,10)
    selected=meaning[mnum]
    print(selected)
    answer=input('이 말의 사자성어는?: ')
    if answer in idioms:
        ans=1
    else:
        print('틀렸습니다... 다시 도전!')
print('맞았습니다. 게임을 종료합니다.')


