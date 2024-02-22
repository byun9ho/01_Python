

s={10,1,3,4}
print(s)

#1. data add

# add() method: add element(s) to set
s.add(100)
print(s)

# update():
s.update([5,6])
print(s)

#2. remove or extract data
# pop

result=s.pop()
print(result)
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

s.update([10,11,12,13,14])
print(s)
# remove
s.remove(10)
print(s)
# s.remove(15) # KeyErr

# discard() 버리다. 카드놀이에서 안 쓰는 카드를 버리다
s.discard(6)
print(s)
print(s.discard(16))
print(s)

# clear()
s.clear()
print(s) # set()을 반환

s1={1,2,3}
s2={3,4,5}
print(s1,s2)
# 합집합: union()   |
print(s1.union(s2))
print(s1|s2)


# 교집합: intersection()
print(s1.intersection(s2))
print(s1&s2)

# 차집합: difference()
print(s1.difference(s2))
print(s1-s2)
print(s2.difference(s1))
print(s2-s1)
