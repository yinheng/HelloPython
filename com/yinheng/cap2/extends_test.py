class People:

    __weight =  65

    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work
        print("People init")

    def say_hello(self):
        print("hello, i am %s, i am %d years old, my job is %s, weight %s" %(self.name, self.age, self.work, People.__weight))

    def __del__(self):
        print("销毁:" + self.__str__())
        self.__sleep()


    # Operator
    def __add__(self, other):
        return "%s&%s" % (self.name, other.name)

    def __sleep(self):
        print("%s sleeping..." % self.name)



# 如果重写了__init__ 时，要继承父类的构造方法，可以使用 super 关键字：
#
# super(子类，self).__init__(参数1，参数2，....)
# 还有一种经典写法：
#
# 父类名称.__init__(self,参数1，参数2，...)

class Singer(People):
    def __init__(self, name, age):
        People.__init__(self, name, age, "SING")
        print("Singer init")



yinheng = Singer("yinheng", 24)
guohao = Singer("guohao", 24)
yinheng.say_hello()

print(yinheng.name)
print(yinheng._People__weight)

print(yinheng + guohao)