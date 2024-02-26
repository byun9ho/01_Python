# number="100"
# def midterm(number):
#     result=""
#     if number.isdigit() is True:
#         if number is 100:
#             if number/10==1:
#                 result=True
#     else:
#         result=False
#     return result

def add_and_mul(a,b,c):
    return b+a*c+b
print(add_and_mul(3,4,5)==63)


def print_coin():
    print('비트코인')


print_coin()


def print_coins():
    for i in range(100):
        print(i + 1, end=' ')
        print_coin()


print_coins()

def mul(x,y):
    return x*y

def toUpper(lcase):
    ucase=lcase.upper()
    # print (ucase)
    return ucase

toUpper(lcase)

def pickup_even(nums):
    global evens
    evens=list()
    # lnums=list(nums)
    for i in range(len(nums)):
        num=int(nums[i])
        if num%2==0:
            evens.append(num)
        else:
            pass
    return evens
n=int(input('Type in numbers :'))
n=str(n)
n=list(n)
pickup_even(n)
print(evens)


