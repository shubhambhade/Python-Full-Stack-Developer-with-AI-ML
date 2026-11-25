class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        # delete instance varible in class
        del self.a

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
# delete instance varible outside of class
del t.b
print(t.__dict__)
