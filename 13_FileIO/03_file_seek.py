#seek(offset,whence) 함수

print('Seek in File(s) : seek() ----')
f=open('data/seek_test_data.txt','r',encoding='utf-8')

f.seek(0,0) #시작위치: 0,0:파일처음
lines=f.read()
print(lines)

f.seek(1,0) #시작위치: 1, 0:파일처음
lines=f.readlines()
print(lines)

f.seek(7,0) #시작위치: 7, 0:파일처음
lines=f.readlines()
print(lines)
f.seek(4,0) #시작위치: 4, 0:파일처음
lines=f.readlines()
print(lines)
f.seek(8,0) #시작위치: , 0:파일처음
lines=f.readline()
print('line',lines)
f.seek(8,0) #시작위치: , 0:파일처음
lines=f.readlines()
print('lines',lines)
f.seek(14,0) #시작위치: , 0:파일처음
lines=f.readlines()
print('lines',lines)
f.seek(16,0) #시작위치: 16, 0:파일처음
lines=f.readlines()
print('lines',lines)
f.seek(19,0) #시작위치: 19, 0:파일처음 UTF-8은 3byte 그래서 16+3=19가 다음글자 위치('나')
lines=f.readlines()
print('lines',lines)
f.seek(22,0) #시작위치: 22, 0:파일처음 UTF-8은 3byte 그래서 16+3+3=22가 다음글자 위치('다')
lines=f.readlines()
print('lines',lines)
# f.seek(19,0) #시작위치: 19, 0:파일처음 UTF-8은 3byte 그래서 16+3=19가 다음글자 위치('나')
# lines=f.readlines()
# print('lines',lines)
