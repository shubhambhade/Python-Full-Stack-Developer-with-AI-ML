class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display_values(self):
        #inside class instance variables access using self variable
        print(self.a)
        print(self.b)

t = Test()
t.display_values()
print()
#outside of class instance variables access using object reference variable
print(t.a)
print(t.b)