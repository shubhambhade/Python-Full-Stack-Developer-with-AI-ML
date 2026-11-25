class Student:
    #static variable
    university_name = "pune university"

    def __init__(self, student_name,roll_number):
        #instance variables
        self.student_name = student_name
        self.roll_number = roll_number

    def info(self):
        x = 10 # local variable
        for i in range(x): # i is local variable
            print(i,end=" ")

student = Student("sham",101)
student.info()