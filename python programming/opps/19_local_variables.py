class Test:
    @staticmethod
    def average(list1):
        result =  sum(list1)//len(list1)
        return result

    @staticmethod
    def wish(name):
        for i in range(5):
            print("Good morning : ",name)

t = Test()
arr = [10,20,30,40]
ans = t.average(arr)
print("average of numbers : ", ans)
print()
t.wish('sham')