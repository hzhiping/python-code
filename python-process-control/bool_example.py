#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 20:39


def bool_expression():
    # 案例
    print(True)
    print(False)
    print(True == 1)
    print(False == 0)
    print(False + True + 100)
    # 使用bool()函数可以将其他值转换为布尔类型
    print(bool(100))
    print(bool("采薇采薇，薇亦作止。"))
    print(bool(""))
    print(bool([100]))
    print(bool([]))
    print(bool())


def bool_example():
    # 布尔表达式的值只有两个：True和False
    x = 108.88
    y = 108.66
    print(x == y)  # 符号'=='用于判断两个数是否相等，这条语句的result=False
    x = 108.66
    print(x == y)  # 这条语句的result=True
    print(x != y)  # 符号!=用于判断两个数是否不相等，这条语句的result=False
    a = 156
    b = 266
    print(a >= b)  # 符号'>='用于判断a是否大于等于b，这条语句的result=False
    print(a <= b)  # 符号'<='用于判断a是否小于等于b，这条语句的result=True
    print(a > b)  # 符号'>'用于判断a是否大于b，这条语句的result=False
    print(a < b)  # 符号'<'用于判断a是否小于b，这条语句的result=True
    a = 'abc'
    b = ' cde'
    print(a > b)  # 也可以对两个字符串进行大小判断，这条语句的result=False
    print(a < b)  # 这条语句的result=True
    # 需要注意操作符“=”和操作符“==”的区别，“=”是将右边的值赋给左边的变量
    # 而“==”是判断左边的值和右边的值是否相等


if __name__ == "__main__":
    bool_example()
