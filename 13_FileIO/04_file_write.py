# 문자열을 파일에 쓰기

# s='''01234
# abcde f
# 가나다라마바
# '''
#
# f=open('data/write_data.txt','w',encoding='utf-8')
# f.write(s)
# f.close()

# 키보드로 입력받은 문자열들을 파일에 쓰기
# s=input('Type in Strings: ')
# f=open('data/write_data2.txt','w',encoding='utf-8')
# f.write(s)
# f.close()

#3 기존의 파일 뒤에 쓰기: 'a' 모드 사용
# s=input('Type in   Strings:  ')
# f=open('data/write_data2.txt','a',encoding='utf-8')
# f.write(s)
# f.close()

s1='''
Line1
Line2
Line3'''
f=open('data/write_data2.txt','a',encoding='utf-8')
f.write(s1)
f.close()

#4 파일을 생성(쓰기)하고 읽기

filename='data/readwrite.txt'
f1=open(filename,'a',encoding='utf-8') #뒤에 계속 붙게
for i in range(5):
    f1.write(input(f'Type {i}th String :')) #5번 반복
# f1.write(s)
f1.close()

f2=open(filename,'r',encoding='utf-8')
print(f2.read())
f2.close()

# 간혹 파일 close를 안하고 계속 작업하는 경우도 많음. 이 경우 메모리를 계속 잡아먹게됨.


