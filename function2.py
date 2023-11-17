# function2.py

print("aaa")

#함수정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

#함수호출
retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

#호출
print(swap(3,4))


#기본값이 있는 함수
def times(a=10, b=20) : 
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자(매개변수명 기술)
def connectURI(server, port) : 
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print(connectURI("multi.com","80"))
print(connectURI(port="8080", server="multi.com"))

#가변인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)

    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))


#람다 함수(이름이 없는 간단한 함수정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

