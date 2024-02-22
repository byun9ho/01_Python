# text1='Python is a programming language'
# text2='and integrate systems more effectively'
#
# text1.lower()



# from datetime import datetime, timedelta, date
# date2=input('날짜 입력(연/월/일):')
# date2=datetime.strptime(date2,'%Y/%m/%d')
# # print(type(date2))
# print(f'10년 뒤: {date2.year+10}년 {date2.month}월 {date2.day}일')

nums=input("숫자를 여러 개 입력하세요.")
for h in range(len(nums)):
	print(int(nums[h])*'\u2665')
