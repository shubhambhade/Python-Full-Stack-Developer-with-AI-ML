class Outer:
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")

        def m1(self):
            print("inner class method")

# outer = Outer()
# inner = outer.Inner()
# inner.m1()

Outer().Inner().m1()