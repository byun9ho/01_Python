import sys
# print(sys.path)
for path in sys.path:
    print(path)

print(type(sys.path))

# 파이썬 모듈 검색 경로
#1. sys.modules
#2. built_in_modules
#3. sys.path ( 위에서 검색한 부분 )

# from show_info1 import * #경로가 설정되어 있지 않은 경우 빨간줄

sys.path.append("C:/workspace_Multi07/01_PythonProject/15_module_package/my_modules")

from show_info1 import *

show_name1()
show_phone1()

for path in sys.path:
    print(path)