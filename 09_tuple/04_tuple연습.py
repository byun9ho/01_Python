# 2 dimension tuple

t=((1,2,3),(4,5,6),(7,8,9))
print(t)

lt=()
for i in range(len(t)):
    # lt1,lt2,lt3=t[i]
    # print(lt1,lt2,lt3)
    temp=t[i]
    lt=list(temp)
    print(lt)

for r in t:
    for c in r:
        print(c, end=' ')
    print()

# print(t[0][1])

for r in range(len(t)):
    for c in range(len(t[r])):
        print(t[r][c],end=' ')
    print()