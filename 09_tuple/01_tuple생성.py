# creating tuple

t1=(1,2,3)
print(t1, type(t1))

# 하나만 가지고 생성시
t01=(1,)
print(t01,type(t01))
t02=1,
print(t02,type(t02))

t2=4,5,6
print(t2, type(t2))

t3=t1,(7,8,9)
print(t3,type(t3))

t4=[1,2],[3,4,5]
print(t4, type(t4))

t5=tuple([1,2,3])
print(t5,type(t5))

t6=tuple('hello')
print(t6,type(t6))

#list > tuple, tuple > list - 원본은 튜플로 바꿔서 지워지지 않게. 작업은 리스트.
list1=[1,2,3]
t7=tuple(list1)
print(list1,t7,type(list1),type(t7))

list2=list(t4)
print(list2,type(list2))