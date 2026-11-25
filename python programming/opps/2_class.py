class Student:
    "class developed by shubham"

    def __init__(self):
        self.name = "shubahm"
        self.roll_number = 101
        self.marks = 98

    def display_student_information(self):
        print("hello i am : ",self.name)
        print("my roll number : ", self.roll_number)
        print("my marks are : ", self.marks)

# how to create object
'reference_variable =  ClassName()'

student  = Student()

# by using reference variable we can access variables and methods of class.
print(student.name)
print(student.roll_number)
print(student.marks)
print()
student.display_student_information()
    