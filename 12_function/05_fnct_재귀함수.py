# 재귀함수 recursive function
# 함수 내부에서 자신의 함수를 다시 호출

def sum(n):
    print(f'print n={n}')
    if n==1:
        return 1
    return n + sum(n-1)
print('sum(10)=',sum(10), id(sum(10)))

def fact1(n):
    result=1
    for i in range(1,n+1):
        result*=i
        print(f'result={result}')
    return result

print('fact1(5)=',fact1(5))

def my_fact2(n):
    if n<=1:
        return 1
    return n*my_fact2(n-1)

print('my_fact(5)=',my_fact2(5))

def outFunc(x,y):
    def inFunc(a,b): #밖에서 호출해서 사용 불가능
        return a+b
    return inFunc(x,y)

print(outFunc(10,30))

#lambda 함수
# 한줄짜리, return 사용하지 않음
# lambda <인수들>:<반환할식>
# 람다함수는 함수참조를 반환
# 변수로 람다함수 객체를 받아서 함수호출한다

f=lambda:1
print('f()=',f())

add=lambda x,y:x+y
print('add(2,3)=',add(2,3))

add=lambda x=10,y=30:x+y #디폴트값 주는 방법
print(add( ))
print(add(10)) #디폴트쓸때
print(add(10,50))
print(add(y=10,x=500))

#람다표현식: 함수이름명명하지않고 바로 호출
# (lambda 매개변수들:식)(인수들)

print((lambda x : x+10)(10))

#(lambda x:y=10;x+y)(10) 람다표현식 안에서는 변수생성불가
#람다표현식 바깥에서 전역변수사용
y=10
print((lambda x:x+y)(10))

def plus_ten(x):
    return x+10

#[1,2,3,4,5]+10

new=[]
for n in [1,2,3,4,5]:
    new.append(n+10)
print('for loop',new)

print('map만 사용',list(map(plus_ten,[1,2,3,4,5]))) #plus_ten이라는 함수에 리스트에 있는 값을 적용해서 결과를 다시 원래 자리로 돌려놓기
print('lambda추가사용',list(map(lambda x:x+10,[1,2,3,4,5])))

# sum elements from 2 lists

def add_list(x,y):
    new_list=[]
    for i in range(len(x)):
        new_list.append(x[i]+y[i])
    return new_list

a=[1,2,3,4]
b=[10,11,12,13]
print('add_list 함수 정의:',add_list(a,b))

#map(func, iterable dataset) 함수: iterable한 데이터 하나하나에 함수 적용

def add_two(x,y):
    return x+y
print('map과 add함수 : ',list(map(add_two, a,b)))

print('map과 lambda : ',list(map(lambda x,y:x+y,a,b)))

