class Test:
    def __init__(self):
        print("Address of object pointed by self : ",id(self))

t = Test()
print("Address of object pointed by t : ",id(t))