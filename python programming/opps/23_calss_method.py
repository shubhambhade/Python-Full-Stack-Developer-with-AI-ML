class Bird:
    wings = 2
    @classmethod
    def fly(cls,name_of_bird):
        print('{} flying with {} wings'.format(name_of_bird,cls.wings))
Bird.fly("parrot")
Bird.fly("egale")
