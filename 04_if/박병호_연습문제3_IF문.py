# 입력받은 십진수를 2진수로 변환하여 출력
'''
dnum=int(input('십진수 입력:'))
bnum_str = ""

while dnum > 0:
    bnum_str = str(dnum%2) + bnum_str
    dnum = dnum // 2
bnum_str="0b"+bnum_str
print('이진수는 ', bnum_str)
'''

hnum_str=input('16진수 한글자 입력 :')
if len(hnum_str) == 1:
    if "A" <= hnum_str < "G" or "a" <= hnum_str < "g":
        hnum = int(hnum_str, 16)
        print('10진수 ==> ', hnum)
    else:
        print('입력하신 ',hnum_str,'은 16진수 글자가 아닙니다')

else:
    print('한글자를 초과하여 입력하셨습니다')

