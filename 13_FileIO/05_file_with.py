# with sentence: close()가 자동으로 수행됨.
# with open(파일명, 모드) as 파일객체:
#       수행문장들
#
# with open('study_data2.txt','r') as f:
#     text=f.read()
#     print(text)
#
# with open('data/file1.txt','a',encoding='utf-8') as f:
#     f.write(text)

with open('data/scores.txt','r',encoding='utf-8') as f:
    data=f.readlines()
    print(data)

with open('data/scores2.txt', 'r', encoding='utf-8') as f:
     data = f.readlines()
     print(data)

score=[]
for i in range(len(data)):
    temp=data[i]
    temp=temp.rstrip('\n')
    score=score+temp.split(',')

print('score',score)