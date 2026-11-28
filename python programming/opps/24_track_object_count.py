class CountTheNumberOfObjects:
    count = 0
    def __init__(self):
        CountTheNumberOfObjects.count  += 1
        
    @classmethod
    def get_number_of_objects(cls):
        print("The Number Of Objects Created : ",cls.count)

CountTheNumberOfObjects.get_number_of_objects()
o1 = CountTheNumberOfObjects()
o2 = CountTheNumberOfObjects()
o3 = CountTheNumberOfObjects()
CountTheNumberOfObjects.get_number_of_objects()
