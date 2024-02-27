# Yesterday 가사가 저장되어 있는 텍스트 파일을 읽어 가사에 사용되고 있는 단어들의  목록을 알파벳 순서로 출력하고,
# 각 단어들이 몇 개씩 사용되고 있는지 단어별 개수를  출력하는 프로그램 작성
# ∙ 리스트, 세트, 딕셔너리 등의 자료구조를 이용
# 단어들은 모두 소문자로 변환하여 사용다.

# path="C:/Users/byung/OneDrive/Documents/1_Personal/2024_멀티잇교육/숙제/01_파이썬/수업자료_20240226/yesterday.txt"
# path='C:/workspace_Multi07/01_PythonProject/13_FileIO/data/yesterday.txt'
#
# lyric=[]
# words=[]
# wordcount=dict()
# wordkey=[]
# lword=dict()
# with open(path,'r',encoding='utf-8') as yday:
#     lyric = yday.readlines()
#     print(lyric)
#     for strNum in range(len(lyric)):
#         phrase=lyric[strNum].lower()
#         word=phrase.split()
#         print(word)
#         words=words+word
#         print(words)
#     for word in words:
#         if word in wordcount:
#             wordcount[word]+=1
#         else:
#             wordcount[word]=1
#     print(wordcount)
#     wordkey=list(wordcount.keys())
#     wordkey.sort()
#     print(wordkey)
#     for keyword in wordkey:
#         lword.update({(keyword):(wordcount[keyword])})
#     for key,value in lword.items():
#         print(f'{key} \t : {value}')



# def my_sum(file_obj,file_name):
#     with open(file_obj,'a',encoding='utf-8') as numfile:
#         numpair=numfile.readlines()
#         print(numpair)
#
# my_sum(path,'..\data\ex9_3_answer.txt')
# readf='C:/workspace_Multi07/01_PythonProject/13_FileIO/data/ex9_3_words.txt'
# writef='C:/workspace_Multi07/01_PythonProject/13_FileIO/data/ex9_3_ans.txt'
# numpair=list()
# nums=list()
# ans=list()
# def my_sum(readf,writef):
#     with open(readf,'r', encoding='utf-8') as numfile:
#         numpair=numfile.readlines()
#         print(numpair)
#         for i in range(len(numpair)):
#             strpair=numpair[i]
#             nums=strpair.split()
#             a=int(nums[0])
#             b=int(nums[1])
#             c=a+b
#
#             ans.append([a,b,c])
#             print(f'{a}+{b}={c}')
#     with open(writef,'w',encoding='utf-8') as wfile:
#         for i in range(len(ans)):
#             w=str(ans[i])+'\n'
#             wfile.write(w)
#         print('file written completed')
#
# my_sum(readf,writef)

# def my_sum(file_obj,file_name):
#     with open(file_obj,'a',encoding='utf-8') as numfile:
#         numpair=numfile.readlines()
#         print(numpair)

# my_sum(path,'..\data\ex9_3_answer.txt')
# readf='C:/workspace_Multi07/01_PythonProject/13_FileIO/data/ex9_3_words.txt'
# writef='C:/workspace_Multi07/01_PythonProject/13_FileIO/data/ex9_3_ans.txt'
numpair=list()
nums=list()
ans=list()
path='data/ex9-3.txt'
def my_sum(numfile,filename):
    with open(filename,'r', encoding='utf-8') as numfile:
        numpair=numfile.readlines()
        print(numpair)
        for i in range(len(numpair)):
            strpair=numpair[i]
            nums=strpair.split()
            a=int(nums[0])
            b=int(nums[1])
            c=a+b

            ans.append([a,b,c])
            print(f'{a}+{b}={c}')
    with open(filename,'w',encoding='utf-8') as wfile:
        for i in range(len(ans)):
            w=str(ans[i])+'\n'
            wfile.write(w)
        print('file written completed')

my_sum(numfile,path)





#4.

# input_member('/data/memlist.txt')

memlist = list()

def input_member(filename):
    with open(filename,'w',encoding='utf-8') as fname1:
    # f.close()
    # open(filename,'a',encoding='utf-8;) as f:
         while True:
            name=input('멤버를 입력하세요.(종료는 q) : ')
            if name=='q':
                choice()
            else:
                name=(str(name)+str('\n'))
                fname1.write(name)

def output_member(filename):
    with open(filename,'r',encoding='utf-8') as fname2:
        memlist=fname2.readlines()
        for i in range(len(memlist)):
            print(memlist[i])
        choice()


def choice():
    job=input('저장 1. 출력 2. 종료 q : ')
    if job=='1':
        input_file=input('멤버 명단을 저장할 파일명을 입력하세요 : ')
        input_member(input_file)
    elif job=='2':
        load_file=input('멤버 명단이 저장된 파일명을 입력하세요. : ')
        output_member(load_file)
    elif job=='q':
        pass
    else:
        choice()

choice()
