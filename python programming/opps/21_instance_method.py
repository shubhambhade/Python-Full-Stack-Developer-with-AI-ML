class Student: 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def diplay_student_info(self):
        print("Name : ",self.name)
        print("Marks : ",self.marks)

    def grade(self):
        if self.marks >= 60:
            print("you got first grade")
        elif self.marks >= 40:
            print("you got second grade")
        else:
            print("failed")

n = int(input("Enter number of student : "))
for i in range(n):
    name = input("Enter Student Name : ")
    marks = int(input("Enter Marks : "))
    student = Student(name,marks)
    student.diplay_student_info()
    student.grade()

    