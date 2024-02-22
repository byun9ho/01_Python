# in / not in
# return true/false if key exist in specified dictionary
d={'nine':9,'ten':10}

print('two' not in d)

#예제

book={}
book['저자']='홍길동'
book['책제목']='파이썬'
book['출판일']='2020-01-30'
book['가격']=25000

#문제 북 딕셔너리 키와 값을 모두 출력하시오

for key in book.keys():
    print('%s : %s' %(key,book[key]))
for key in book.keys():
    print('{0} : {1}'.format(key,book[key]))
for key in book.keys():
    print(f'{key} : {book[key]}')
for key in book.keys():
    print(key,' : ',book[key])

bkeys=book.keys()
#print(bkeys)
for cat in bkeys:
    content=book.get(cat)
    print(f'{cat} : {content}')
