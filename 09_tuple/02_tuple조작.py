# tuple 조작

#1 인덱싱

t=1,2,3,4,5,6,7,8
print(t[0])

#2 슬라이싱

print(t[:])
print(t[3:])
print(t[::-1])

#3 +연산
t1=(4,5,6)
t2=10,11,12
t3=t1+t2
print(t3)

#4. *연산
t4=t1*3
print(t1*3)

#5 멤버연산: in / not in
t5='hello','hi','hohoh'
print('hi' in t5)  # True/False 출력

#6 길이 len()
print(len(t4))

# 튜플 삭제들
#t5[0]='hahaha' # TypeError: 'tuple' object does not support item assignment
# del(t5[0])  #TypeError: 'tuple' object doesn't support item deletion
#deletion tuple itself ok
del(t5)

#7 search tuple element: index(), count()

t6=tuple('hello hi how are you!')
print(t6)
print(t6.index('o'))
print(t6.count('h'))