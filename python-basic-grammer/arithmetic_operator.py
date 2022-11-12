#!/usr/bin/env python
# encoding: utf-8
# author: hzhiping
# datetime: 2022/11/12 16:44

def arithmetic_operator():
    x = 10
    y = 12
    # 加法运算
    a = x + y
    print("a的值为：", a)
    # 减法运算
    a = x - y
    print("a 的值为：", a)
    # 乘法运算
    a = x * y
    print("a 的值为：", a)
    # 除法运算
    a = x / y
    print("a 的值为：", a)
    # 取模运算
    a = x % y
    print("a 的值为：", a)
    # 修改变量x 、y、z
    x = 10
    y = 12
    z = x ** y
    print("z 的值为：", z)
    # 整除运算
    x = 15
    y = 3
    z = x // y
    print("z 的值为：", z)


if __name__ == '__main__':
    arithmetic_operator()
