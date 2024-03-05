# try:
#     for i in range(1, 7):
#         result = 7 // i
#         print(result)
# except ZeroDivisionError:
#     print("Not divided by 0")
# finally:
#         print("종료되었습니다.")
#
# sentence = list("Hello Gachon")
# while (len(sentence) + 1):
#     try:
#         print(sentence.pop(0))
#     except Exception as e:
#         print(e)
#         break
#
# from calculator import *

alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(a)
    print(b)
    print(b[a])
print("*"*50)

alist = ["a", "1", "c"]
blist = ["b", "2", "d"]
for a, b in enumerate(zip(alist, blist)):
    print(a)
    print(b)
    # print(a/int(b[0]))

# import random
# answer = random.randint(1,10)
# def guess_number(answer):
#     try:
#         guess = int(input("숫자를 넣어 주세요: "))
#         if answer == guess:
#             print("정답!")
#         else:
#             print("틀렸습니다.")
#     except ValueError:
#         print("숫자가 아닙니다.")
#
# guess_number(answer)

for i in range(3): # 0,1,2
    try:
        print(i, 3// i) # 0, 3//0, 3//1, 3//2 >
    except ZeroDivisionError:
        print("Not divided by 0")





