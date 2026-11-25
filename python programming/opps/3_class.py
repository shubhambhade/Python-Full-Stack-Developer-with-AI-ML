"information varried from student to student"

class Student():

    def __init__(self, name, roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_student_information(self):
        print("Student Name : ", self.name)
        print("Student Roll NUmber : ",self.roll_number)
        print("Student Marks : ",self.marks)

student = Student("sham", 101, 90)
student.display_student_information()
print()
student1 = Student("ram",102,56)
student1.display_student_information()
