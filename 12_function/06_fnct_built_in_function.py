


print(abs(-10))


#
# print(all([0,1,2,3]))
# print(any(a,0,'',[]) #하나라도 트루이면 트루
#
# print(chr(65))
# print(ord('A'))
#
# #divmod(), pow()
# #min(), max(), sum()
# print(max([1,2,3,4,-10]))
# print(min([1,2,3,4,-10]))
# print(sum([1,2,3,4,-10]))

#enumerate()
print(list(enumerate(['kim','lee','choi'])))
data=['kim','lee','choi']
for item in enumerate(data):
    print(item)
for idx,value in enumerate(data):
    print(idx,value)

#eval: 쓰여진 그대로 실행

print(eval('10'))
print(eval('10*10'))
print(eval('10'+'10'))

#filter: 함수에 입력되었을 때 만족하는 값들만 결과

def positive(x):
    return x>0 #양수만반환

#filter(): 반복가능한 함수에 자료를 적용하여 True인 결과만 추출


print(positive(10))
print(positive(-10))
print(list(map(positive,[1,2,-1,10,-5])))
print(list(filter(positive,[1,2,-1,10,-5])))
# print(filter(positive,[0,-1,5,-7,10]))
# print(list(filter(positive,[0,-1,5,-7,10]))

def even(x):
    if x%2==0:
        return x

print(list(filter(even,[1,2,-1,10-5])))

#help()
help(print)
help(filter)

#sorted

#int(), float(), str()
#bin(),hex(),oct()
#input(),print()
#zip(),map()
#range()
#len()
#list(),tuple(), dict(), set()
#id(),type()
#lambda
