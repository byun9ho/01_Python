#
# first_value=0
# second_value=0
# for i in range(1,10):
#     if i == 5:
#         print('1st If')
#         continue #for에 물려있음.
#         first_value=i
#     print('Move to 2nd with: ',i)
#     if i == 10:
#         print('2nd If')
#         break
#         second_value=i
# print(first_value+second_value)

# coupon=0
# money=200000
# coffee=3500
# cnt=0
# while money>coffee:
#     if coupon < 4:
#         money=money-coffee
#         coupon+=1
#     else:
#         money+=2800
#         coupon=0
#     cnt+=1
#     print('남은 돈',money)
# print(money)

# for i in range(5,0,-1):
#     for j in range(i):
#         print('*')
#     print('\n')

for i in range(1,9,2):
    for j in range(5-i):
        print(" ")
    print('*')

space=' '
star='*'
for i in range(5):
    for a in range(4-i):
        print(space, end='')
    for b in range(i*2+1):
        print(star, end='')
    print()

for i in range(5):
    print(space*(4-i)+star*(i*2+1))

for i in range(1,10,2):
    print("{0:^10}".format())

