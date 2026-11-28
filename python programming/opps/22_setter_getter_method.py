class Student:
    def set_name(self,name):
        self.name = name
    def set_marks(self,marks):
        self.marks = marks
    def get_name(self):
        return self.name 
    def get_marks(self):
        return self.marks

n = int(input("Enter number of student : "))
students = []
for i in range(n):
    s = Student()
    name = input("Enter Student Name : ")
    marks = int(input("Enter Marks : "))
    s.set_name(name)
    s.set_marks(marks)
    students.append(s)
print()
for s in students:
    print("Student Name : ",s.get_name())
    print("Marks : ",s.get_marks())
    print()