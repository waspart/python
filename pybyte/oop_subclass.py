class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initializing SchoolMember: {}".format(self.name))

    def tell(self):
        print('Name: {}, age: {}'.format(self.name, self.age), end='  ')

class Teacher(SchoolMember):
    """docstring for Teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initializing Teacher: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {:d}".format(self.salary))

class Student(object):
    """docstring for Student"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initializing Student: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {:d}".format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()

members = [t, s]
for member in members:
    member.tell()
