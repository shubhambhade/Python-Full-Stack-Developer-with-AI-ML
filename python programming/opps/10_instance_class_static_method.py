class Student:
    university_name = 'pune university'

    def __init__(self, student_name, roll_number):
        self.student_name = student_name
        self.roll_number = roll_number

    #instance method
    def display_student_information(self):
        print("Name Of Student : ", self.student_name)
        print("Roll Number Of Student : ", self.roll_number)

    @classmethod
    def display_university_name(cls):
        print("University Name : ", cls.university_name)

    @staticmethod
    def getSum(sub1 , sub2):
        return sub1 + sub2

student = Student("pratik",1)
student.display_student_information()
student.display_university_name()
print("Total Marks : ",student.getSum(50,90))