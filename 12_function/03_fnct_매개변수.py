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



