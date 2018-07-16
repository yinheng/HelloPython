class People:
    'This is a test, to define a class'

    peopleCount = 0

    def __init__(self, name, age, area):
        self.name = name
        self.age = age
        self.area = area
        People.peopleCount += 1

    def __del__(self):
        print(self, "销毁")


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def say(self):
        print("I am saying %s" % self.name)

yinheng = People(age=24, area="CHN", name="yinheng")
guohao = People("guohao", 26, "USA")

print(yinheng.get_age())
print(yinheng.get_name())

print(guohao.get_age())

print(People.peopleCount)

print(yinheng.__class__)
print(yinheng.__dict__)
print(yinheng.__doc__)

yinheng.say()
guohao.say()