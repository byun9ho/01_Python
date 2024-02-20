# 과제코드

P=0
Z=0
N=0
for t in range(10):
    prompt='숫자'+str(t+1)+'입력 : '
    #KeyIn=int(input(f'숫자{t}입력 : '))
    #KeyIn=int(input('숫자'+str(t+1)+'입력 :'))
    KeyIn = int(input(prompt))
    if KeyIn > 0:
        P+=1
    elif KeyIn < 0:
        N+=1
    else:
        Z+=1
print('----------------')
print('양의 개수 : ',P)
print('음의 개수 : ',N)
print('0의 개수 : ',Z)

