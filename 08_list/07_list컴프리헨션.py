# num_list=[]
# for num in range(1,6):
#     num_list.append(num)
# print(num_list)
#
# num_list=[num for num in range(1,6)]

#문제 1-20중 짝수만으로 구성된 리스트

even=[num for num in range(2,21,2)]
print(even)

even=[]

even=[num for  num in range(1,21) if num%2==0]
print(even)

for num in range(1,21):
    if num%2==0:
        even.append(num)

#문제 1-20중 3의 배수

triple=[num for num in range(3,21,3)]
print(triple)

num_lis4=[num for num in range(1,21) if num%3==0]
print(num_lis4)

list1=[1,2,3,4,10,11,12]
num_list5=[num for num in list1 if num%3==0]
print(num_list5)

foods=['Teok', 'Jja', 'Ramyun', 'Pizza']
sides=['Dakuan','Kimchi','Pickle']

for food, side in zip(sides, foods, strict=False):
    print(food, '--',side)

for item in zip(foods, sides):
    print(item)

name=['Hong','Kang','Seong','Bangja']
sex=['M','M','F','M']
addr=['SEL','HanYang','Dokdo','Busan']

print(list(zip(name,sex,addr))) #이게 zip
print('-----')

ob=zip(name,sex,addr)
ob_list=list(ob)
print(ob_list)