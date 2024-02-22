#set

#1 no sequence: 입력순서 출력순서 다를 수도
#2 동일한 요소(값)는 중복될 수 없다
#3 인덱스 사용 불가
#4 요소 추가/삭제 가능
#5 변경가능한 항목을 세트의 요소로 가질 수 없음
#  리스트를 세트의 요소로 가질 수 없음
#  튜플은 포함

#키만 모아놓은 딕셔너리의 특수한 형태
#세트(집합) 생성: {}. set()

#세트생성
s1={1,2,3,4,5,1,2,4} #redundant byebye
print(s1, type(s1))

s2=set([10,8,11,20,30,10])
print(s2)

s3=set((10,20,300))
print(s3)

s4=set({'one':1,'two':2})
print(s4)

# s1[0] TypeError: 'set' object is not subscriptable    ~~~^^^ 문제점 위치

# 리스트는 세트의 요소가 될 수 없다
# s5={1,2,[4,3]}
# TypeError: unhashable type: 'list'

# hashable type --> hashing
# 객체를 식별할 수 있는 코드를 부여 - 테이블에 저장: 키, 값
