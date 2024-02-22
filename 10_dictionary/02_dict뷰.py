# view

d={'one':1,'two':2,'three':3}
keys=d.keys()
print(keys,type(keys))

print(list(keys))

# printing values to keys

for key in d.keys():
    print(key,d[key])

values=d.values()
print(values,type(values),list(values),tuple(values))
print(len(values))

for value in d.values():
    print(value,end=' ')
print()

items=d.items()
print(items,type(items))
print(list(items))

for item in d.items():
    print(item,type(item))


print('언패킹처럼')
for key,item in d.items():
    print(key,item,type(key),type(item))


univ={'학번':'1000','이름':'홍길동','학과':'컴퓨터학과'}
print(f'학생정보: {univ}')
print('')
univ['연락처']='010-1111-1111'
print(f'학생정보+연락처: {univ}')
print('')
univ['학과']='파이썬학과'
print(f'학생정보 중 학과변경: {univ}')
print('')
del(univ['학과'])
print(f'학생정보 중 힉과삭제: {univ}')
