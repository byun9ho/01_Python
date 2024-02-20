#` 문자열 대소문자 변환
# upper(), lower(), title() 단어별 대문자 , capitalize() 첫글자 대문자

text1='Python is great!'
text2="Yes, it is."
text3 = "It's not like any other"

print(f'text1: {text1}')
print(f'text2: {text2}')
print(f'text3: {text3}')


print('대문자로',text1.upper())
print('소문자로',text2.lower())
print('단어별 시작문자 대문자',text2.lower().title())
print('문장 첫글자 대문자',text1.upper().capitalize())
print('Swapcase()',text1.swapcase())


#2 문자열 검색
# count(단어), find(단어), rfind(), index() 단어시작위치인덱스를 가져옴, rindex(), startswidth()

text4='I like python, i like swimming, i like hotdog'
print('count(): ',text1.count('python'))
print('count(): ',text1.count('Python'))
print('count(): ',text1.count('Python'))
print('count(): ',text4.count('like'))

print('find(): ',text4.find('like')) # 인덱스반환(첫번째로 만난 위치)
print('rfind(): ',text4.rfind('like')) # 인덱스반환(첫번째로 만난 위치) find와 rfind가 같으면 같은 숫자. 다르면 다른 숫자
print('find(): ',text1.find('Python')) # 인덱스반환(첫번째로 만난 위치)
print('find()',text1.find('melon'))
print('index():',text4.index('like'))
#print('index()',text1.index('like')) # 찾는 문자열이 없는 경우 오류 발생. 그래서 index보다 find를 써라
print('startswith():',text4.startswith('i like')) #논리값반환
print('startswith():',text4.startswith('I like')) #논리값반환
print('endswith():',text4.startswith('i like')) #논리값반환
print('endswith():',text4.endswith('.')) #논리값반환
print('startswith():',text4.startswith('I like',7))

#3 문자열 치환, 편집
# strip() 양쪽지우기, rstrip(), lstrip(): 공백문자(지정문자) 제거
# replace(): 문자치환

text5='         ham haha hotdog!       '
print(text5)
text6='<><><>hoho>>>>>!'
text7='<><><>hoho>>>>>'
print(text6)
print('strip():',text5.strip())
print('lstrip():',text5.lstrip())
print('rstrip():',text5.rstrip())
print('strip(<>):',text6.strip('<>')) # 요 모양에 맞는 것을 제거
print('strip(<>):',text7.strip('<>')) # 요 모양에 맞는 것을 제거
print('strip(>):',text6.strip('>'))
print('strip(>):',text7.strip('>'))
print('replace()',text5.replace('ham','hom'))

#4 문자열을 분리/결합

print(text4)
print('split():',text4.split())
print('split():',text4.split(',')) # ,기준으로 자름
print('rsplit():',text4.rsplit())

text8='apple banana kiwi'
data = text8.split()
print(data)
print('join():', '-'.join(data)) # join은 문법이 기존 것들과 차이 교체할 것.join(대상)
print('join():', '/'.join(data))
print('join():', ' '.join(data))
print('join():', ''.join(data))

text9='''firstline
.. secondline
.. thirdline
'''
print(text9.split()) # 줄 바꿈도 잘라지는 기준
print(text9.split('\n'))
print(text9.split('\n',2))
print(text9.split('\n', maxsplit=1 ))
print(text9.splitlines())

#5 문자열 정렬

# 왼쪽정렬, 오른쪽정렬, 서식(포맷)에서의 정렬 ^ < > 외에 함수가 있음
# center(), ljust(), rjust()

print('center():',text8.center(30))
print('ljust():',text8.ljust(30,'='))
print('rjust():',text8.rjust(30,'='))



#6 문자열 판단: 숫자, 알파벳, ...
# isdigit(), isdecimal(), isalpha(), ...

print('1234','1234'.isdigit())
print('1234','1234'.isalpha())
print('abc한글'.isalpha())
print('1234***'.isalnum())
print('hello'.isupper())
print('hello'.islower())
print('hello'.istitle())
print('Hello hoho'.istitle())

# Unicode: \u0101 백슬래시 + 16진수

print('\u0101')
print('\u0101','\0063','\u000a', '\u0011', '\u2665', '\u2668')