class Student:
    def __init__(self, name, roll_number, marks):
        # creating instance variables and initializing variables
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

student = Student("sham",101,98)
student1 = Student("ram",102,78)
print(student.name," ", student.roll_number," ", student.marks)
print()
print(student1.name," ", student1.roll_number," ", student1.marks)
