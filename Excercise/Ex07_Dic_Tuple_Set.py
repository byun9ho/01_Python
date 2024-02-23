# students=[
# {"name":"홍길동","Korean":87,"Math":98,"English":88,"Science":95},
# {"name":"이몽룡","Korean":92,"Math":98,"English":96,"Science":98},
# {"name":"성춘향","Korean":76,"Math":96,"English":94,"Science":90},
# {"name":"변학도","Korean":98,"Math":92,"English":96,"Science":92},
# {"name":"박지성","Korean":95,"Math":98,"English":98,"Science":98},
# {"name":"류현진","Korean":64,"Math":88,"English":92,"Science":92}
# ]
# std={}
#
# print('이름\t총점\t평균')
# for cnt in range(len(students)):
#     std=students[cnt]
#     total=int(std["Korean"])+int(std["Math"])+int(std["English"])+int(std["Science"])
#     avg=total/4
#     std["합계"]=total
#     std["평균"]=avg
#     students[cnt]=std
#     print(std['name'],'\t',std["합계"],'\t',std["평균"])
    # print(students[cnt])
    # std=students[(cnt)]
    # skey=std.keys()
    # print(dict[skey[0]])
    # ckey=skey[1::]
    # for cls in ckey:
    #     ttl=ttl+get(cls)
    # avg=ttl/len(ckey)
    # # students[cnt]{"총점":ttl,"평균":avg}

# engdic=dict()
# i,j=0,0
#
# while i==0:
#     eword=input('영어 단어 등록 (종료는 quit) :')
#     if eword=='quit':
#         i=1
#     else:
#         if engdic.get(eword,0) == 0:
#             edef=input(f'{eword}의 뜻 입력 (종료는 quit) :')
#             while edef != 'quit':
#                 engdic[eword]=edef
#                 break
#         else:
#             print(f'{eword}는 이미 등록된 단어입니다.')
#
# while j==0:
#     eword2=input('검색할 단어 입력 (종료는 quit) :')
#     if eword2=='quit':
#         j=1
#     else:
#         edef2=engdic.get(eword2,0)
#         if edef2 == 0:
#             print(f'{eword2}는 사전에 없는 단어입니다.')
#         else:
#             print(f'{eword2}의 뜻은 {edef2}입니다.')
# print('종료합니다.')









