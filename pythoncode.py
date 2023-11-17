# Person 클래스 정의
class Person:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def printInfo(self):
        print("Person Info (ID: {}, Title: {})".format(self.id, self.title))

# Manager 클래스 정의 (Person 클래스를 상속)
class Manager(Person):
    def __init__(self, id, title, skill):
        # 부모 클래스의 생성자 호출하여 공통 속성 초기화
        super().__init__(id, title)
        # 자식 클래스의 고유한 속성 초기화
        self.skill = skill

    def printInfo(self):
        # 부모 클래스의 printInfo() 메서드 호출 및 자식 클래스의 속성 출력
        super().printInfo()
        print("Manager Info (Skill: {})".format(self.skill))

# Employee 클래스 정의 (Person 클래스를 상속)
class Employee(Person):
    def __init__(self, id, title, role):
        # 부모 클래스의 생성자 호출하여 공통 속성 초기화
        super().__init__(id, title)
        # 자식 클래스의 고유한 속성 초기화
        self.role = role

    def printInfo(self):
        # 부모 클래스의 printInfo() 메서드 호출 및 자식 클래스의 속성 출력
        super().printInfo()
        print("Employee Info (Role: {})".format(self.role))


# Sample 1
person1 = Person(101, "John Doe")
person1.printInfo()

# Sample 2
manager1 = Manager(201, "Manager", "Leadership")
manager1.printInfo()

# Sample 3
employee1 = Employee(301, "Employee", "Developer")
employee1.printInfo()

# Sample 4
manager2 = Manager(202, "Senior Manager", "Project Management")
manager2.printInfo()

# Sample 5
employee2 = Employee(302, "Senior Developer", "Lead Developer")
employee2.printInfo()

# Sample 6
person2 = Person(102, "Jane Doe")
person2.printInfo()

# Sample 7
manager3 = Manager(203, "Technical Manager", "Technical Leadership")
manager3.printInfo()

# Sample 8
employee3 = Employee(303, "Software Engineer", "Software Developer")
employee3.printInfo()

# Sample 9
person3 = Person(103, "Alice Smith")
person3.printInfo()

# Sample 10
employee4 = Employee(304, "System Architect", "System Design Lead")
employee4.printInfo()