# Person 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        # 생성자 메서드: 인스턴스 변수 초기화
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        # 인스턴스 정보를 출력하는 메서드
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

# Student 클래스 정의 (Person 클래스를 상속)
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # 부모 클래스의 생성자 호출하여 공통 속성 초기화
        super().__init__(name, phoneNumber)
        # 자식 클래스의 고유한 속성 초기화
        self.subject = subject
        self.studentID = studentID

# Person 클래스의 인스턴스 생성
p = Person("전우치", "010-222-1234")

# Student 클래스의 인스턴스 생성
s = Student("이순신", "010-111-1234", "컴공", "991122")

# 각 클래스의 인스턴스의 속성을 출력
print(p.__dict__)  # Person 클래스의 인스턴스 속성 출력
print(s.__dict__)  # Student 클래스의 인스턴스 속성 출력

