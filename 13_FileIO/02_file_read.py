# 텍스트파일 읽기

# 텍스트파일 생성: 메모장
# study_data.txt

#1 파일열기(open) - 기본모드는 read

f=open('data/study_data.txt', mode='r', encoding='utf-8')
# encoding 안 알려줄때 오류: UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 0: illegal multibyte sequence

# f=open('study_data3.txt',mode='r',encoding='utf-8')

#2 파일처리(읽기)
# text=f.read()
# text=f.readline()
# print(text)
# text2=f.readline()
# print(text2)

# while True:
#     text=f.readline()
#     if not text: # 읽을 내용이 없으면(마지막)
#         break
#     print(text)

# print(f.readlines())

# for textline in f.readlines():
#     # print(textline, end='')
#     print(textline)

for textline in f:
    print(textline, end='')

# for textline in f:
    # textline=textline.strip()
    # textline=textline.rstrip()
    # print(textline)
    # print(textline, end='')

#3: 파일닫기(close())
f.close()

#영문으로된텍스트읽기
# print('English Text Reading')
# f1=open('study_data2.txt',mode='r')
# text=f1.read()
# print(text)
# f1.close()

#  seek(): 내 탐색위치 지정