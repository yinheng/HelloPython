# str = input("请输入：")
# print("你输入的内容是: ", str)
import os

fo = open("hello.py0000", "a+")
print(fo.name)
print(fo.mode)
print(fo.closed)
print(fo.encoding.title())
print(fo.write("122\n1099jmbnmbnmbnmjjjjjjjjjjj212123------------------------"))
print(fo.seek(0, 0))
print("read" + fo.read())

fo.close()

os.remove("hello.txt")
os.rename("hello.py0000", "hello.txt")

print(os.getcwd())


