

scores=[[90,85,70],[88,79,92],[100,100,100],[90,60,70]]

print(f'----성적표---------')
for indsc in range(len(scores)):
    print(list(scores[indsc:indsc+1]))

print(f'-----성적표(점수, 총점, 평균)-----')

i=0
for indsc in scores:
    total = 0
    for sc in indsc:
        total += sc
    avg=total/len(indsc)
    print(list(scores[i:i+1]),total,'%.2f'%avg)
    i+=1
#



