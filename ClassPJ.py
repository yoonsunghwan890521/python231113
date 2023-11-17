# Class 연습
# 1) 클래스를 정의

class Person:
    def __init__(self):
        self.name = "default Name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스를 정의
p1 = Person()
p2 = Person()
p1.name = "Yoon"

#3) 메서드 호출
p1.print()
p2.print()

#런타임(코드가 실행중)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)


