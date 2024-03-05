#
# with open('s.txt','r') as f:
#     data=f.readlines()
# print(data)
# sort_data=sorted(data)
#
# for d in sort_data:
#     print(d,end='\n')
# print()
#
# def word_count(filename):
#     with open(filename,'r') as f:
#         yesterday=f.readlines() # 쭉 읽고
#     words=[]
#     for line in yesterday: #위의 라인단위로 읽어서 쪼개 버리면 공백과 개행문자 제거
#         line=line.split() # 스플릿하고 소문자로 바꿔서 넣음.
#         for w in line:
#             words.append(w.lower()) # 줄 단위로 쪼개서 소문자로 바꾼 단어단위로 워드에 리스트 저장
#
#     wordList=list(set(words))
#     wordList.sort()
#
#     wordDict=dict()
#     for w in wordList:
#         wordDict[w]=words.count(w)
#
#     for key,value in wordDict.items():
#         print(key,value)
#
# word_count('yesterday.txt')
# #=================
# with open() as f:
#     while True:
#         text=f.readline()
#         if not text:
#             break
#         word=text.lower().strip('\n').strip(' ')
#         for i in word:
#             my_list1.append(i)
#
#     my_list2=sorted(my_list1)
#     for k in range(my_list2.count('')):
#         my_list2.remove('')
#
#     my_list3=[]
#     for j in my_list2:
#         if j not in my_list3:
#             my_list3.append(j)
#         else:
#             pass
#
#     for p in my_list3:
# #=======

# with open('yesterday.txt','r') as f:
#     data=f.read().lower().split()
# word={}
# for voca in data:
#     if voca in word:
#         word[voca]+=1
#     else:
#         word[voca]=1
#
# for voca,count in sorted(word.items()):
#     print(f'{voca}:{count}')
#
# # ====
# # .strip('\n').split(' ') = .split()
#
# value1=value1 if val1>=- else f'({value1})'
#
#
# #======================
# def my_sum(file_name):
#     with open(file_name, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#
#     with open(file_name, 'w', encoding='utf-8') as f:
#         for line in lines:
#             numbers = sum(map(float, line.split()))
#             f.write(str(numbers)+'\n')
#
#
# my_sum('sum.txt')
# #======================
# def my_sum(filename, data_list='r'):
#     with open(filename, 'r') as f:
#         data = f.readlines()
#     for i in data:
#         s = i.split(' ')
#         add = int(s[0]) + int(s[1])
#         print(f'{s[0]}+{s[1]}={add}')
#
# my_sum('data/mysum.txt', 'r')
# #======================
# def my_sum(input_file, name):
#     with open(input_file,'r') as f:
#         rst = ''
#         for data in f.readlines():
#             a = int(data.split(' ')[0])
#             b = int(data.split(' ')[1])
#             rst += f"{a}+{b}={a+b:.1f}\n"
#         w = open(name, 'w', encoding='utf-8')
#         w.write(rst)
#
# input_file = 'data/number.txt'
# my_sum(input_file, 'result.txt')
#======================
print('#9-4','='*50)