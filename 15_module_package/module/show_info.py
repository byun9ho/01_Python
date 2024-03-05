def show_name():
    print('홍길동')

def show_phone():
    print('010-1234-1234')

if __name__ == '__main__': # 모듈 자체를 실행하는 경우에 대해. 만약 다른 파이썬 코드에 의해 호출되는 경우 메인이 아니게 됨.
    print('자신의 모듈 show_info를 호출함')
    show_name()
    show_phone()