# 리스트 삭제

a=[10,20,30]
b=[1,2,3]
c=['apple','coconut','melon','hotdog']

#1) 리스트 한 값 삭제
print(f'alist: before deletion {a}')
del(a[1])
print(f'alist: after deletion {a}')

print(f'blist: before deletion {b}')
b[1:2]=[]
print(f'blist: after deletion {b}')

#2) delete 'list' itself

a.append(50)
b.append(5)
print(f'alist: before del : {a}')
a=[] # value empty
print(f'alist: after del: {a}')
print(f'a type: {type(a)}')

print(f'blist: before del : {b}')
b=Noneb # None type but b remains
print(f'blist: after del: {b}')
print(f'b type: {type(b)}')

print(f'clist: before del : {c}')
del(c) # remove from memory. No "c" No variable C
print(f'clist: after del: {c}')
print(f'c type: {type(c)}')


