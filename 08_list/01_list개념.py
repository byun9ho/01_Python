#
# 4개 정수 입력 받아 합계와 평균 출력

# num1=int(input('1번째 숫자: '))
# num2=int(input('2번째 숫자: '))
# num3=int(input('3번째 숫자: '))
# num4=int(input('4번째 숫자: '))

# total = num1 + num2 + num3 + num4

# n=4
# total=0
# for i in range(n):
#     num=int(input(f'{i+1}th number: '))
#     total += num
#
# avg=total/(i+1)
# print(f'Total: {total}, Average: {avg}')

#입력된 데이터를 보관하고 있지 않음. num의 값이 매번 입력될 떄 바뀌고 마지막 것만 기억.



# n=4
# total=0
# num_list=[] # num_list=list()
# print(num_list)
# for i in range(n):
#     num=int(input(f'{i+1}th number: '))
#     num_list.append(num)
#     total += num
#
# avg=total/n
#
# print(f'Total: {total}, Average: {avg}')
# print('num_list =',num_list)
#
# for num in num_list:
#     print(num)

# lists=[1,2,3,[1,3],[5,6,7]]
# print(lists)
# print(lists[0], lists[-1])

#리스트생성: [], list()
#리스트 요소 추가: append()
#리스트길이: len(리스트)

# aList=list()
# print(aList)
# for i in range(10):
#     print(aList)
#     aList.append(i)
# print(aList)

# for와 list

#리스트에 입력한 데이터 저장

n=4
total=0
num_list=[] # num_list=list()
print(num_list)
for i in range(n):
    num=int(input(f'{i+1}th number: '))
    num_list.append(num)

#리스트 데이터를 이용해 계산

for x in num_list:
    total+=x

# for num in num_list:
#     total+=num
#     # total = num_list[0] + ... 대신
# for i in range(num_list)):
#     total += num_list(i)

avg=total/n

print(f'Total: {total}, Average: {avg}')
print('num_list =',num_list)

for i in range(len(num_list)):
    print(num_list[i])

for x in num_list:
    print(x)
