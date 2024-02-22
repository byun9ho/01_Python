#zip()

foods=['Teok','Jja','Pizza','Ramyun']
sides=['Kimchi','Dan','Pickle']

zip_list=list(zip(foods,sides))
zip_disc=dict(zip(foods,sides))
print(zip_list)
print(zip_disc)

# list comprehension

xlist=[x*2 for x in range(1,11)]
print(xlist)

ylist=[x+y for x in range(1,11) for y in range(11,21)]
print(ylist, '\n', len(ylist))

foodlist=[(x,y) for x in ['Rice','Noodle','Jja'] for y in ['Kimchi','Dan']]
print(foodlist, '\n', len(foodlist))

print([x+y for x in range(1,5) for y in range(10,15)])
# 세트 컴프리헨션
ySet={x+y for x in range(1,5) for y in range(10,15)}
print(ySet, '\n', len(ySet))

# Dictionary Comprehension
print({food:side for food in foods for side in sides}) #키 값이 유일한 것만 남김. 그래서 가장 마지막의 피클하고만 짝이 됨.

stds=['Chul','Young','Gil','Soon']
std_dic={std:0 for std in stds}
print(std_dic)
print(std_dic.items())

stds={'Chul':90,'Young':50,'Gil':60,'Soon':100}
std_scores={name:'pass' if score>60 else 'FAIL'
            for name, score in stds.items()}

std_scores2=dict()
for name,score in stds.items():
    if score>60:
        std_scores2[name]='pass'
    else:
        std_scores2[name]='FAIL'
print(std_scores)
print(std_scores2)

x=[1,2]
y=x
y.extend([3])
print(x)
print(y)

x=[1,2]
y=x.copy()
y.extend([3])
print(x)
print(y)
