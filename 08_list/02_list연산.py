#1 인덱싱: 요소접근

a=[1,2,3,4,5]
print(a[0],a[-1],a[3])

a=[1,2,3,4,5]
b=[[1,2],3,[5,6]]
print(a[0],a[-1],a[3])
print(b[0],b[2],b[0][0]) #리스트 안 리스트는 순서대로 인덱스를 쭉 쓴다

#2 슬라이싱: 부분문자열

print('a[:]',a[:])
print('a[1:]',a[1:])
print('a[:2]',a[:2])
print('a[::2]',a[::2])
print('a[::-1]',a[::-1])
print('a[::]',a[::])

#3 리스트값변경: using index to access ex. a[i]= specific value

print('a list before change ',a)
a[1]=100
print('a list after change',a)

a[2]=[10,20]
print('a list after change',a)

# Using Slicing
a[1:2]=[30,40]
print('a list after change',a)

c=[10,20,30]
x,y,z=c # 오른쪽 리스트값이 순서대로 변수에 할당됨
print(x,y,z)

#4 merging lists: +
a=[1,2,3,4]
b=[7,8,[9,10]]
print('a+b=',a+b)

#5 리스트 곱하기(multiplying lists)
print('a*3=',a*3)

#6 copy list
a=10 # direct형
b=a
print('a=',a,'b=',b)
b=15
print('a=',a,'b=',b)

print('----------')
print('\n\n')

a_list=[10,20,30,40]
b_list=a_list #shallow copy - a나 b리스트 모두 주소만 가지고 있어서, 둘 중 하나를 바꾸면 다른 것도 바뀜.
c_list=list(a_list) # 제대로 복사

print('a_list:',a_list, 'b_list',b_list,'c_list',c_list)
print('id(a_list):',id(a_list),'id(b_list):',id(b_list),'id(c_list):',id(c_list))


print('----------')

a_list[0]='apple'
print("a_list[0]='apple'")
print('id(a_list):',id(a_list),'id(b_list):',id(b_list),'id(c_list):',id(c_list))
print('a_list:',a_list, 'b_list',b_list,'c_list',c_list)
print('----------')
b_list[-1]='banana'
print("b_list[-1]='banana'")
print('id(a_list):',id(a_list),'id(b_list):',id(b_list),'id(c_list):',id(c_list))
print('a_list:',a_list, 'b_list',b_list,'c_list',c_list)


