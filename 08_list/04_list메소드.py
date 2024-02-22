

#1. append

a=[]
a.append('apple')
a.append('hotdog')
a.append(10)
print(f'alist {a}')

#2. pop(index=-1) 꺼내다.

# value=a.pop()
# print(f'alist:')



#3. sort(): elements sorted
b=[6,3,5,1,-3]
print(f'blist: {b}')
b.sort()
print(f'sort applied: {b}')

#4. reverse(): reverse the order of elements
# b.reverse()
# a.reverse()
# print(f'reverse applied to b: {b}')
# print(f'reverse applied to a: {a}')

#5. index():  리스트에서 지정한 값의 위치를 반환, else no value, ValueError
c=['Hong','Kang','Chunhyang','Byun','Kang']
idx = c.index('Kang')
print(f'{idx}')
# idx=c.index('Bin')
# print(f'{idx}')

#6. insert
print(f'clist before insert {c}')
c.insert(-1,'Bin') # -1의 의미 > 제일 뒷 요소의 바로 앞에 끼워넣기
print(f'clist after insert {c}')

print(f'clist before insert {c}')
c.insert(2,'Picaso')
print(f'clist after insert {c}')

#7. remove(value): remove specified value from the list
#8. count(value): count specified value
print(f'clist before remove Kang {c}')
# c.remove('Kang') #첫번째만 지움. 여러개 원하면 for 이용함.
for item in range(c.count('Kang')):
    c.remove('Kang')
    print(f'clist after remove Kang {c}')
# print(f'clist after remove Kang {c}')

#9. extend(): extend list, adding list to list? > changed to one list
print(f'blist {b}')
b.extend([10,11,12])
print(f'blist after extend([10,11,12]) {b}')
b.append([10,11,12])
print(f'blist after append([10,11,12]) {b}')
b.insert(3, [10,11,12])
print(f'blist after insert(3,[10,11,12]) {b}')
b=b+[10,11,12]
print(f'blist after "+" {b}')
# b.extend(100) # 값 하나는 오류

#10. Sorted() builtin function.
#a=['apple','hotdog','melon']
a=[3,1,-10,11,2]
print(f'alist {a}')
new_a=sorted(a, reverse=True)
print(f'alist after sorted() {a}')
print(f'new_a sorted from alist {new_a}')

#11. copy(): copy list
cpy_a=a.copy()
print(f'alist before copy {a}')
cpy_a.sort()
print(f'cpy_alist after copy {cpy_a}')

#12. clear() claring list. empty list
# cpy_a.clear() # cpy_a[:]=[]와 같음
# print(f'cpy_alist after clear {cpy_a}')

#13. del(): delete specific elements in the list or delete whole list

del(cpy_a[3:])
print(f'cpy_alist {cpy_a}')
# del cpy_a
# print(f'cpy_alist del cpy_a {cpy_a}')

#14. len(): builtin function. return the length of the list = number of elements
print(f'alist len() {len(a)}')
