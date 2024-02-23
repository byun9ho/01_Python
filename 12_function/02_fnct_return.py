# function/return

def get_area():
    w=int(input('Width : '))
    h=int(input('Height: '))
    result=w*h
    print(f'Square width = {w}, height = {h}, Area {result}')
    return result
#
# print(get_area())
#
# def multi_return():
#     return 1,2,3 # 튜플로 만들어져서 리턴

# value=multi_return()
# w,h,area=value
# print(value,type(value))
# print(w,h,area)

def get_names():
    names=[]
    for i in range(3):
        name=input('Name? : ')
        names.append(name)
    return names #리스트형태로 리턴

names=get_names()
print(names)

def get_info():
    name=input('Name: ')
    age=input('Age: ')
    info={'name':name,'age':age}
    return info #딕셔너리형태로 리턴

info=get_info()
print(info,type(info))

