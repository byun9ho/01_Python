# 복수개 자료 치환

a,b=1,2
print(a,b,type(a),type(b))

a,b=b,a,b
print(a,b)

(a,b),(c,d)=(10,11),(12,13)
print(a,b,c,d)

# packing
t=1,2,'hello'
print(t)

# unpacking
x,y,z=t
print(type(t))
print(x,y,z, type(x),type(y),type(z))

t2=(1,2,3,4,5)
a,*b=t2 # *가 붙으면 여러개의 요소를 가진 변수(대표적으로 리스트)로 본다. a에는 1 나머지는 묶어서 b에 저장
print(a,b,type(a),type(b))
a,b,*c=t2
print(a,b,c,type(a),type(b),type(c))
*a,b,c=t2
print(a,b,c,type(a),type(b),type(c))
# *a,*b,c=t2 #SyntaxError: multiple starred expressions in assignment
# print(a,b,c,type(a),type(b),type(c))