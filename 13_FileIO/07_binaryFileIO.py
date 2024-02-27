# binary file: 이진파일
# - text가 아닌 bit단위로 의미가 부여되는 파일
# - 텍스트파일을 제외한 파일:
# - 텍스트파일과 이진파일 구분:

inStr=''

path1="C:/Windows/notepad.exe"
path2='data/notepad.exe'

inF=open(path1,'rb')
outF=open(path2,'wb')

while True:
    inStr=inF.read(1)
    print(inStr)
    if not inStr:
        break
    outF.write(inStr)

inF.close()
outF.close()

