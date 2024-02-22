# #답3)
#
# str1 = 'this is'
# str2 = 'PythON'
# print(str1.title() + ' ' + str2.upper())
# 결과: This is PYTHON

#답4)
# txtOut=''
# ch=''
# txtIn=input('문자열을 입력하세요 : ')
# for idx in range(len(txtIn)):
#     ch=txtIn[idx]
#     if ch=='':
#         ch='$'
#         txtOut += ch
# else:
#     pass
#     txtOut += ch

#답코드
# for ch in txtIn:
#         if ch is 'o':
#             txtOut += '$'
#         else:
#             txtOut += ch

# print(txtOut)

#답5)
# from datetime import date,timedelta 10년후 계산이라 쓸 필요가 없었음
# momentIn=input('날짜(연/월/일) 입력 : ')
# temp=momentIn.split('/')
# year=int(temp[0])
# month=int(temp[1])
# date=int(temp[2])
# year10=year+10
# print(f'입력한 날짜의 10년 후 => {year10}년 {month}월 {date}일')
#
# #답6)
heartrepeats=[]
heartnum=input('숫자를 여러개 입력하세요.')
# heartrepeats=list(heartnum)
# for i in range(len(heartrepeats)):
h='\u2665'
for i in heartnum:
    print( h*int(i) )
    # print(prtheart, '\n')