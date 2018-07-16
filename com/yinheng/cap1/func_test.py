def test(a):
    a = a + 1
    return a

b = 2
test(b)
print(test(b))

#不定长参数函数
def printInfo(*vars):
    print("输出：")
    for var in vars:
        print(var)
    return

printInfo(10, 20, 30, 40)
printInfo(50)

#匿名函数
sumTest = lambda arg1, arg2: arg1 + arg2
print(sumTest(1, 1))