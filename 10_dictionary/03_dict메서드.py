#1. method get()

d={'one':1,'two':2,'three':3}

print('d()',d)
print(f"d['two']:{d['two']}")

print(f"d.get('two'):{d.get('two')}")

# print(d['four']) #KeyError: 'four'

print(f"d.get('four'):{d.get('four')}") # 키에 맞는 값이 없을 때 오류가 아니라 None을 리턴
print(f"d.get('four'):{d.get('four')}",4) # 키에 맞는 답이 없을 때 4를 반환

#2. setdefault() method
d={'one':1,'two':2,'three':3}
print('d()',d)
d={'one':1,'two':2,'three':3}
d.setdefault('two') # key'two' is already with 2, then nothing happen
d.setdefault('four',4) # if no values for key 'four', then value=4
print(f'd.setdefault(two):{d.setdefault('two')}') # key'two' is already with 2, then nothing happen
print(f'd.setdefault(two,20):{d.setdefault('two',20)}') # key'two' is already with 2, then nothing happen
print(f'd.setdefault(four,4):{d.setdefault('four',4)}') # if no values for key 'four', then value=4

print('d()',d)

#3. pop(), popitem() method
d={'one':1,'two':2,'three':3}
print(d.popitem())
key,value=d.popitem()
print(f'key={key}, value={value}')
print(d)

#d={'one':1,'two':2,'three':3}
d['six']=6
d['ten']=10
print(d)

print('dpop() and get()')
#result=d.pop() #TypeError: pop expected at least 1 argument, got 0
#result=d.pop('two')
result=d.get("two")
print(result)
print(d)

#4 copy()
d2=d.copy()
print(d, id(d))
print(d2,id(d2))
d2['four']=4
print(d)
print(d2)

#5 update()
d3={'five':5,'two':2,'seven':7}
print(d3)
d3.update(d2)
print(d3)

#6 clear()
print('6 CLEAR')
print(d,id(d))
d.clear() #그자리에 그대로 비움
print(d,id(d))

print(d2, id(d2))
d2={} #새로운 자리에 d2 생김
print(d2,id(d2))
