# 지역변수 전역변수
'''
a=10 #전역변수 global variables
print(a)

def show_info(name):
    age=10 #지역변수 local variables
    print(name,age)

# print(age)

def show1():
    a=1
    a=a+1
    print(f'a: {a},id(a)')

# def show2():
#     a=a+1 # a 변수 못찾아 오류발생
#     print(f'a: {a},id(a)')

def show1():
    b=a+1 #a: 전역변수
    a=a+1
    print(f'a: {a},id(a)')
    print(f'지역변수 b: {b},id(b)')

def show4():
    global a #전역변수선언
    a=a+1
    print(f'a: {a},id(a)')

show1()
'''

def sub(x,y):
    a=7 #지역변수
    x,y=y,x #스왑
    b=3 #지역변수
    print(a,b,x,y)

a,b,x,y=1,2,3,4 #전역변수
sub(x,y)
print(a,b,x,y) #전역변수만 남은 상태 > 1234

def sub(x,y):
    global b
    global z
    a=7 #지역변수
    x,y=y,x #스왑
    b=3 #지역변수
    z=4
    print('함수내',a,b,x,y)

a,b,x,y=1,2,3,4 #전역변수
print('처음정의',a,b,x,y)
sub(x,y)
print('함수호출후',a,b,x,y) #전역변수만 남은 상태 > 1234

# def show_list(my_list): # my_list는 변수가 아니라 매개변수(파라메터), shallow copy처럼 작동
#     cpy_list=my_list.copy()
#     cpy_list[-1]=100
#     print('cpy_list',cpy_list, id(cpy_list))
#
def show_list(cpy_list): # my_list는 변수가 아니라 매개변수(파라메터), shallow copy처럼 작동
    cpy_list[-1]=100
    print('cpy_list',cpy_list, id(cpy_list))

my_list=[1,2,3,4]
show_list(my_list)
print('my_list',my_list,id(my_list))



