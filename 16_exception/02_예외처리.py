# 예외처리 형식
# try:
#     예외 발생 가능한 문장들
# except:
#     예외처리
# else:
#     예외 발생하지 않는 경우 처리 문장
# finally:
#     예외와 솬계 없이 항상 실행

# try:
#     # print(10/0)
#     print('나이'+23+'살')
# except: # 일단 처리는 가능하지만, 무슨 에러인지 찾지 못함. 위의 2가지가 서로 다르지만 구별 안함.
#     print('오류발생')

# 구체적인 오류 담당하는 에러클래스를 이용하여 처리
# 에러종류 명시

# try:
#     에러발생가능한 문장들
# except 에러담당클래스명 as 에러메시지변수명:
#     에러처리 문장들

try:
    # print(10/0)
    print('나이' + 23 + '살')
    print(10/0)
except ZeroDivisionError as e: # 에러메시지 변수를 활용하여 출력: 에러담당클래스 as 변수명
    print('0으로 나눌 수 없습니다.',e) # e를 통해 에러 메시지 표시함.
except TypeError as e:
    print('잘못 입력된 형식입니다',e)
# 예외 처리 문장을 여러개 쓸 수 있으나 결국 첫번째 만나는 오류만 표시

try:
    num=int(input('숫자입력: '))
    print(num)
except ValueError as e:
    # print('Not number(s)',e)
    pass
else:
    num=num+10
    print(num)
    print('오류가 없습니다')
finally:
    print('종료-------')
