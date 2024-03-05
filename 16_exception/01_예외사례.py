#zero division error

# 10/0 # ZeroDivisionError: division by zero

# print('나이는'+23+'살') #     print('나이는'+23+'살')
        #                            ~~~~~~~~^~~
#                               TypeError: can only concatenate str (not "int") to str

#NameError
# print(b)

# ValueError: incomplete format
# c=100
# print('%d%' % c)
# print('%d%%' % c)

# SyntaxError
# if x > 10
#     print('hello')

# IndexError: 5번 인덱스 없음.
# a=[1,2,3,4]
# print(a[5])

# UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
# def add():
#     a=a+1
#
# add()

# ModuleNotFoundError: No module named 'myModul'
# import myModul

# FileNotFound: FileNotFoundError: [Errno 2] No such file or directory: 'except.txt'
# with open('except.txt','r') as f:
#     f.read()

# OSError: [Errno 22] Invalid argument: 'c:\x0cile\\except.txt'
# with open('c:\file\except.txt','r') as f: # \f 가 의미가 있음.
#     f.read()

