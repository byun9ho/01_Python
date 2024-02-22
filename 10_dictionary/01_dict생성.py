# creating dict
# group data, no sequence
# item= key:value 딕셔너리변수={키1:값1,키2:값2,...)
# accessing value via key

# d={}
d=dict()
print(d,type(d))

d2={1:'a',2:'b',3:'c'}
print(d2,type(d2))
# order of key - no meaning. filled as it gets generated
# key and value can be defined by a user. No restrictions apply
# key should be unique (alphanumeric ok)
# value can be redundant

print(d2[1]) # [key] 1 is not an index
#print(d2[0]) #KeyError: 0

d2[1]=10
print(d2)

#4 adding elements - dic_value[keyn]=valuen

d2[4]=100
print(d2)

#5 key should be unique
d3={'a':1,'b':100, 'c':'hello','b':1000} #키가 중복될 경우, 해당키에는 가장 마지막 입력된 값만 가짐
print(d3)

#6. 밸류값은 하나 또는 여러개의 집합적 자료를 가질 수 있음.
d4={'name':['kim','hong','lee'],
    'score':[100,90,80],
    'gender':['F','M','M'],
    'phone':('123-234','123-9092','010-123-1111')
    }
print(d4)
print(d4['name'])

#7. deleting element(s) del()
del(d4['gender'])
print(d4)
