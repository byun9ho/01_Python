#1. 문자열의 모든 글자 뒤에 $ 붙이기

s='파이썬짱!'
temp=''

for ch in s:
    temp = temp + ch + '$'
    print(temp)

print(temp)

s='파이썬짱!'
temp=''

for ch in s:
    temp = ch + '$' + temp
    print(temp)

print(temp)

s='파이썬짱!'
temp=''

for ch in s:
    temp = '$' +ch+ temp
    print(temp)

print(temp)

s='파이썬짱!'
temp=''

for ch in s:
    temp += ch + '$'
    print(temp)

print(temp)

#2 문자열의 짝수번째

# 제출 후 예시로 사용됨.

s='파이썬은재미있어요'
cnt=-1
temp=''

for ch in s:
    if cnt%2==0:
        ch='#'
    else:
        pass
    temp = temp + ch
#    print(temp)
    cnt+=1

print(temp)

#### 제출된 답안

for i in s[::2]:
    print(i, end='#')

# 작동 안함
temp=''
for i in s[::2]:
    temp+=i+'#'
print(temp)


# 답안
temp=''
for i in range(len(s)):
    ch = '#' if (i%2!=0) else s[i]
    temp+=ch
print(temp)

#3 입력받는문자열을 거꾸로 출력하기

text=input('문자열을 입력하세요 : ')
rev=text[::-1]
print(rev)





