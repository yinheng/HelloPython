#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as e:
        print("参数没有包含数字", e)

# 调用函数
temp_convert("xyz")


try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("Error: 没有找到文件或读取文件失败")
    pass

