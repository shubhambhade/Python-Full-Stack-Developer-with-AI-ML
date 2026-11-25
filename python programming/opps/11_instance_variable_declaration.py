class Test:
    # inside constructor
    def __init__(self):
        # instance variables
        self.a =  10
        self.b = 20

    #inside instance method
    def m1(self):
        #instance variable
        self.c = 30

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
#instance variable outside of class
t.d = 40
print(t.__dict__)

