# function parameters 매개변수 argument 인자
# 매개변수: 함수로 전달되는 값을 갖는 변수(함수정의)
# 인수: 함수를 호출할 때 전달되는 값

def get_area(width,height):

    result=width * height
    print(f'Square width = {width}, height = {height}, Area {result}')
    return result

print(get_area(10,20))

# 사칙연산 수행 함수 정의
# add(a,b): 두수 더하기 a+b
# sub(a,b): 빼기 a-b
# mul(a,b): 곱셈 a*b
# div(a,b): 나눗셈 a/b

# def add(a,b):
#     add_result=a+b
#     print(f'a{a}+b{b}={add_result}')
#     return add_result
# def sub(a,b):
#     sub_result1=a-b
#     sub_result2=b-a
#     print(f'a{a}-b{b}={sub_result}') # or b{b}-{a}={sub_result2}')
#     return sub_result1 #,sub_result2
# def mul(a,b):
#     mul_result=a*b
#     print(f'a{a}*b{b}={mul_result}')
#     return mul_result
# def div(a,b):
#     div_result1=a/b
#     div_result2=b/a
#     print(f'a{a}/b{b}={div_result1} or b{b}/{a}={div_result2}')
#     return div_result1,div_result2
#
# a=9
# b=(3)
# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)

# print(add(a,b))
# print(sub(a,b))
# print(mul(a,b))
# print(div(a,b))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    # while b!=0:
    #     return a/b
    # return 0
    if b == 0:
        print('divided by 0')
        return ''
    else:
        return a/b

a=9
b=(3)
print(add(a,b))
print(sub(a,b))
print(mul(a,b))
print(div(a,b))
print(div(a,0))

# default parameter(s) - 디폴트매개변수는 마지막에 위치해야 함

def greet(name,msg='Hello'):
# def greet(msg='Hello',name)  #SyntaxError: parameter without a default follows parameter with a default
    print(name+','+msg)

greet('Hong','Hi')
greet('Hong')

print('hi',end=' ')
print('hi')
#print(end=' ','hi') #SyntaxError: positional argument follows keyword argument

#3 Positional parameters 위치 매개변수
# 매개변수의 위치가 실인수로 전달받을 때 동일한 위치의 변수에 저장됨.
# 매개변수의 순서대로 위치가 전달됨.
# def add(a,b):
#     pass
# add(3,5)

def show_names(names):
    for name in names:
        print(name,end=' ')

show_names(['Hong','Shim','Kang']) # 리스트로 매개변수 넘길 수 있음
print()

def show_info(info):
    print(info)
    # for n in info.keys():
    #     print(info[n])
    for key,value in info.items():
        print(key,info[key])

info={'이름':'홍길동','나이':20} # 딕셔너리로 전달
show_info(info)

#5 가변길이 매개변수
# 매개변수의 길이가 정해지지 않는 경우 여러개의 값을 전달 받을 때 사용
#  *args 매개변수, **kwargs 키워드아귀먼트 kwargs=> key=value 형태

#1 *args 매개변수

#print('hi','ho', end='\') # end는 매개변수 이름

def my_sum(*args):
    total=0
    for arg in args:
        total+=arg
    return total

total=my_sum(1,2)
print(total)
total=my_sum(1)
print(total)
total=my_sum(1,2,3)
print(total)
total=my_sum(1,3,4,5,6)
print(total)

#2) **kwargs 매개변수

# def info(**kwargs):
#     pass
print('------------------------')
def show_info(**kwargs):
    for key in kwargs.keys():
        print(key,end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs.items():
        print(item)

show_info(id='abc')
show_info(id='abcd',name='hong')
show_info(id='abcd',name='hong',age=30)

#6 keyword arguments 키워드인수
# 인수 앞에 키워드를 두어서 인수를 구별, 인수의 위치가 매개변수의 위치와 달라도 됨
def my_print(a,b,c):
    print(a)
    print(b)
    print(c)

my_print(10,30,40) #입력하는 위치가 중요
my_print(a=5,c=10,b=30) #매개변수이름을 직접 지정해주면 키워드인수(키워드매개변수)
# my_print(c=10,30,2) 이거 안됨.

def show_info2(id,name,age): #명시적
    print(id)
    print(name)
    print(age)

show_info2('123','hong',30)
show_info2(id='123',age=30,name='hong')

# *args는 **kwargs앞에 반드시 와야 함. *args는 가변길이 매개변수지만 실제 쓸때는 위치매개변수
def my_func(*args,**kwargs):
    pass

#def my_func(**kwargs,*args): #*args는 포지셔널 매개변수
#   pass

my_func(1,2,3,a=10,b=3)
my_func(1,a=10,b=3)

# 가변인수 사용시: 위치인수 다음에 키워드인수(해석: 키워드전까지는 몽땅 위치인수로 인식, 이후는 키워드인식)


