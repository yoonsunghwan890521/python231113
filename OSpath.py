from os.path import *
import glob
import os

print(dir())

print(abspath("demo.py"))
print(basename("c:\\work2\\demo.py"))

fName = "c:\\python310\\python.exe"

if exists(fName):
    print("파일크기: {0}".format(getsize(fName)))
else:
    print("파일 없음")

result = glob.glob("c:\\work2\\*.py")
for i in result:
    print(i)


print("운영체제이름:{0}".format(os.name))
print("환경변수:{0}".format(os.environ))

#os.system("notepad.exe")

os.chdir("..")