#!/usr/bin/python
# -*- coding: UTF-8 -*-

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    Money = 1000
    #global Money
    Money = Money + 1
    return Money


print(Money)

print(AddMoney())