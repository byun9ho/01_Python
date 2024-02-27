#파일 로드해서 첫번째 컬럼 기준으로 정렬 후 저장

lmeat=list()
dmeat=dict()
dm=dict()
keys=list()
mkey,mvalue=('','')
path='data/s.txt'
with open(path,'r',encoding='utf-8') as fmeat:
    meat=fmeat.readlines()
    for i in range(len(meat)):
        mstring=meat[i]
        mkey,mvalue=mstring.split()
        dmeat.update({mkey:mvalue})
        print(dmeat)
    keys=list(dmeat.keys())
    keys.sort()
    for idx in keys:
        dm[idx]=dmeat[idx]
    print(dm)
meatlist=dm.items()
lmeat=list(meatlist)
for i in range(len(lmeat)):
    item=str(lmeat[i])
    # print(item)
    item=item.lstrip("('")
    item=item.rstrip(")'")
    item=item.replace("', '"," ")
    print(item)






    

#
# print(lmeat)
# for item in meatlist:
#     pitem=str(item)
#     pitem=pitem.replace("'","")
#     pitem=pitem.replace(",","")
#     pitem=pitem.replace
#     print(pitem)

    # print(ldm)
    # for i in range(5):
    #     fmeat.write())  # 5번 반복
    # # f1.write(s)
    # f1.close()



    # print(meat)
    # rownum=len(meat)
    # for i in range(rownum):
    #     lmeat=list(meat[i].replace('\n',''))
    #     # lmeat=meat[i].rstrip('\n')
    #     print(lmeat)
    #     # lmeat=lmeat.split()
    #     mkey,mvalue=str(lmeat[0]),str(lmeat[1])
    #     dmeat[mkey]=mvalue
    # key=list(dmeat.keys())
    # key.sort()
    # print(key)
    # for idx in key:
    #     dm[idx]=dmeat[idx]
    # print(dm)
    #
    #



# f1=open(filename,'a',encoding='utf-8') #뒤에 계속 붙게
# for i in range(5):
#     f1.write(input(f'Type {i}th String :')) #5번 반복
# # f1.write(s)
# f1.close()
#
# with open(path,'rb') as f:
#     data_pickle=load(f)
#
# for item in data_pickle:
#     print(item)
#
# data_pickle.append(['종로구',321673,300000,21673])
#
# print(data_pickle)

#회원명단 파일을 생성하고 읽기
# 파일이름 mem.txt

