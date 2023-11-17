#11월 15일 수업용

import testmodule as tm

tm.defaultvalue = 100

print(tm.defaultvalue)

#DemoFormat.py

for i in range(1,11):
    URL = "http://multi.com/?page="+str(i)
    print(URL)

print("----숫자출력----")

for x in range(1,6):
    print(x,"*",x,"*",x*x)

for x in range(1,6):
    print(x,"*",x,"*",str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"*",str(x*x).zfill(5))