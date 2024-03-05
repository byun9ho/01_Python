# import show_info

# show_info.show_name()
# show_info.show_phone()

# from show_info import show_name,show_phone
#
# show_name() # 필요로 하는 함수만 부를 땐 모듈이름 필요없음
# show_phone()

import show_info as si # aliasing

si.show_phone()

from show_info import *

show_name()

# from show_info import show_name as sn
# sn()

from show_info import show_phone as sp
sp()
show_phone()




